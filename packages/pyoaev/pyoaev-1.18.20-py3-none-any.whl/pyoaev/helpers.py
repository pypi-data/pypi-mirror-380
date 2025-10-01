import base64
import json
import os
import os.path
import re
import sched
import ssl
import tempfile
import threading
import time
import traceback
from typing import Callable, Dict, List

import pika
from thefuzz import fuzz

from pyoaev import OpenAEV, utils
from pyoaev.configuration import Configuration
from pyoaev.daemons import CollectorDaemon
from pyoaev.exceptions import ConfigurationError

TRUTHY: List[str] = ["yes", "true", "True"]
FALSY: List[str] = ["no", "false", "False"]


# As cert must be written in files to be loaded in ssl context
# Creates a temporary file in the most secure manner possible
def data_to_temp_file(data):
    # The file is readable and writable only by the creating user ID.
    # If the operating system uses permission bits to indicate whether a
    # file is executable, the file is executable by no one. The file
    # descriptor is not inherited by children of this process.
    file_descriptor, file_path = tempfile.mkstemp()
    with os.fdopen(file_descriptor, "w") as open_file:
        open_file.write(data)
        open_file.close()
    return file_path


def is_memory_certificate(certificate):
    return certificate.startswith("-----BEGIN")


def ssl_cert_chain(ssl_context, cert_data, key_data, passphrase):
    if cert_data is None:
        return

    cert_file_path = None
    key_file_path = None

    # Cert loading
    if cert_data is not None and is_memory_certificate(cert_data):
        cert_file_path = data_to_temp_file(cert_data)
    cert = cert_file_path if cert_file_path is not None else cert_data

    # Key loading
    if key_data is not None and is_memory_certificate(key_data):
        key_file_path = data_to_temp_file(key_data)
    key = key_file_path if key_file_path is not None else key_data

    # Load cert
    ssl_context.load_cert_chain(cert, key, passphrase)
    # Remove temp files
    if cert_file_path is not None:
        os.unlink(cert_file_path)
    if key_file_path is not None:
        os.unlink(key_file_path)


def ssl_verify_locations(ssl_context, certdata):
    if certdata is None:
        return

    if is_memory_certificate(certdata):
        ssl_context.load_verify_locations(cadata=certdata)
    else:
        ssl_context.load_verify_locations(cafile=certdata)


def create_mq_ssl_context(config) -> ssl.SSLContext:
    config_obj = Configuration(
        config_hints={
            "MQ_USE_SSL_CA": {
                "env": "MQ_USE_SSL_CA",
                "file_path": ["mq", "use_ssl_ca"],
            },
            "MQ_USE_SSL_CERT": {
                "env": "MQ_USE_SSL_CERT",
                "file_path": ["mq", "use_ssl_cert"],
            },
            "MQ_USE_SSL_KEY": {
                "env": "MQ_USE_SSL_KEY",
                "file_path": ["mq", "use_ssl_key"],
            },
            "MQ_USE_SSL_REJECT_UNAUTHORIZED": {
                "env": "MQ_USE_SSL_REJECT_UNAUTHORIZED",
                "file_path": ["mq", "use_ssl_reject_unauthorized"],
                "is_number": False,
                "default": False,
            },
            "MQ_USE_SSL_PASSPHRASE": {
                "env": "MQ_USE_SSL_PASSPHRASE",
                "file_path": ["mq", "use_ssl_passphrase"],
            },
        },
        config_values=config,
    )
    use_ssl_ca = config_obj.get("MQ_USE_SSL_CA")
    use_ssl_cert = config_obj.get("MQ_USE_SSL_CERT")
    use_ssl_key = config_obj.get("MQ_USE_SSL_KEY")
    use_ssl_reject_unauthorized = config_obj.get("MQ_USE_SSL_REJECT_UNAUTHORIZED")
    use_ssl_passphrase = config_obj.get("MQ_USE_SSL_PASSPHRASE")
    ssl_context = ssl.create_default_context()
    # If no rejection allowed, use private function to generate unverified context
    if not use_ssl_reject_unauthorized:
        # noinspection PyUnresolvedReferences,PyProtectedMember
        ssl_context = ssl._create_unverified_context()
    ssl_verify_locations(ssl_context, use_ssl_ca)
    # Thanks to https://bugs.python.org/issue16487 is not possible today to easily use memory pem
    # in SSL context. We need to write it to a temporary file before
    ssl_cert_chain(ssl_context, use_ssl_cert, use_ssl_key, use_ssl_passphrase)
    return ssl_context


class ListenQueue(threading.Thread):
    def __init__(
        self,
        config: Dict,
        injector_config,
        logger,
        callback,
    ) -> None:
        threading.Thread.__init__(self)
        self.pika_credentials = None
        self.pika_parameters = None
        self.pika_connection = None
        self.channel = None

        self.callback = callback
        self.config = config
        self.logger = logger
        self.host = injector_config.connection["host"]
        self.vhost = injector_config.connection["vhost"]
        self.use_ssl = injector_config.connection["use_ssl"]
        self.port = injector_config.connection["port"]
        self.user = injector_config.connection["user"]
        self.password = injector_config.connection["pass"]
        self.queue_name = injector_config.listen
        self.exit_event = threading.Event()
        self.thread = None

    # noinspection PyUnusedLocal
    def _process_message(self, channel, method, properties, body) -> None:
        """process a message from the rabbit queue

        :param channel: channel instance
        :type channel: callable
        :param method: message methods
        :type method: callable
        :param properties: unused
        :type properties: str
        :param body: message body (data)
        :type body: str or bytes or bytearray
        """
        json_data = json.loads(body)
        # Message should be ack before processing as we don't own the processing
        # Not ACK the message here may lead to infinite re-deliver if the connector is broken
        # Also ACK, will not have any impact on the blocking aspect of the following functions
        channel.basic_ack(delivery_tag=method.delivery_tag)
        self.thread = threading.Thread(target=self._data_handler, args=[json_data])
        self.thread.start()

    def _data_handler(self, json_data) -> None:
        self.callback(json_data)

    def run(self) -> None:
        self.logger.info("Starting ListenQueue thread")
        while not self.exit_event.is_set():
            try:
                self.logger.info("ListenQueue connecting to RabbitMQ.")
                # Connect the broker
                self.pika_credentials = pika.PlainCredentials(self.user, self.password)
                self.pika_parameters = pika.ConnectionParameters(
                    host=self.host,
                    port=self.port,
                    virtual_host=self.vhost,
                    credentials=self.pika_credentials,
                    ssl_options=(
                        pika.SSLOptions(create_mq_ssl_context(self.config), self.host)
                        if self.use_ssl
                        else None
                    ),
                )
                self.pika_connection = pika.BlockingConnection(self.pika_parameters)
                self.channel = self.pika_connection.channel()
                try:
                    # confirm_delivery is only for cluster mode rabbitMQ
                    # when not in cluster mode this line raise an exception
                    self.channel.confirm_delivery()
                except Exception as err:  # pylint: disable=broad-except
                    self.logger.error(str(err))
                self.channel.basic_qos(prefetch_count=1)
                assert self.channel is not None
                self.channel.basic_consume(
                    queue=self.queue_name, on_message_callback=self._process_message
                )
                self.channel.start_consuming()
            except Exception:  # pylint: disable=broad-except
                try:
                    self.pika_connection.close()
                except Exception as errInException:
                    self.logger.error(str(errInException))
                traceback.print_exc()
                # Wait some time and then retry ListenQueue again.
                time.sleep(10)

    def stop(self):
        self.logger.info("Preparing ListenQueue for clean shutdown")
        self.exit_event.set()
        self.pika_connection.close()
        if self.thread:
            self.thread.join()


class PingAlive(utils.PingAlive):
    pass


### DEPRECATED
class OpenAEVConfigHelper:
    def __init__(self, base_path, variables: Dict):
        self.__config_obj = Configuration(
            config_hints=variables,
            config_file_path=os.path.join(
                os.path.dirname(os.path.abspath(base_path)), "config.yml"
            ),
        )

    def get_conf(self, variable, is_number=None, default=None, required=None):
        result = None
        try:
            result = (
                self.__config_obj.get(variable)
                if (self.__config_obj.get(variable) is not None)
                else default
            )
        except ConfigurationError:
            result = default
        finally:
            if result is None and default is None and required:
                raise ValueError(
                    f"Could not find required key {variable} with no available default."
                )
            return result

    def to_configuration(self):
        return self.__config_obj


### DEPRECATED
class OpenAEVCollectorHelper:
    def __init__(
        self,
        config: OpenAEVConfigHelper,
        icon,
        collector_type=None,
        security_platform_type=None,
        connect_run_and_terminate: bool = False,
    ) -> None:
        config_obj = config.to_configuration()
        # ensure the icon path is set in config
        config_obj.set("collector_icon_filepath", icon)
        # override the platform in config if passed this way
        if security_platform_type is not None:
            config_obj.set("collector_platform", security_platform_type)

        self.__daemon = CollectorDaemon(
            configuration=config_obj,
            callback=None,
            collector_type=collector_type,
        )

        self.__daemon.logger.warning(
            f"DEPRECATED: this collector should be migrated to use {CollectorDaemon}."
        )

        self.logger_class = utils.logger(
            config.get_conf("collector_log_level", default="error").upper(),
            config.get_conf("collector_json_logging", default=True),
        )
        self.collector_logger = self.logger_class(config.get_conf("collector_name"))
        self.api = self.__daemon.api
        self.config_helper = config
        self.config = {
            "collector_id": config_obj.get("collector_id"),
            "collector_name": config_obj.get("collector_name"),
            "collector_type": collector_type,
            "collector_period": config_obj.get("collector_period"),
        }

    def schedule(self, message_callback, delay):
        # backwards compatibility: when older style call sets delay
        # and no config exists,
        if self.__daemon._configuration.get("collector_period") is None:
            self.__daemon._configuration.set("collector_period", delay)
        self.__daemon.set_callback(message_callback)
        self.__daemon.start()


class OpenAEVInjectorHelper:
    def __init__(self, config: OpenAEVConfigHelper, icon) -> None:
        self.api = OpenAEV(
            url=config.get_conf("openaev_url"),
            token=config.get_conf("openaev_token"),
        )
        # Get the mq configuration from api
        self.config = {
            "injector_id": config.get_conf("injector_id"),
            "injector_name": config.get_conf("injector_name"),
            "injector_type": config.get_conf("injector_type"),
            "injector_contracts": config.get_conf("injector_contracts"),
            "injector_custom_contracts": config.get_conf(
                "injector_custom_contracts", default=False
            ),
            "injector_category": config.get_conf("injector_category", default=None),
            "injector_executor_commands": config.get_conf(
                "injector_executor_commands", default=None
            ),
            "injector_executor_clear_commands": config.get_conf(
                "injector_executor_clear_commands", default=None
            ),
        }

        self.logger_class = utils.logger(
            config.get_conf("injector_log_level", default="error").upper(),
            config.get_conf("injector_json_logging", default=True),
        )
        self.injector_logger = self.logger_class(config.get_conf("injector_name"))

        icon_name = config.get_conf("injector_type") + ".png"
        injector_icon = (icon_name, icon, "image/png")
        self.injector_config = self.api.injector.create(self.config, injector_icon)
        self.connect_run_and_terminate = False
        self.scheduler = sched.scheduler(time.time, time.sleep)
        # Start ping thread
        if not self.connect_run_and_terminate:
            self.ping = PingAlive(
                self.api, self.config, self.injector_logger, "injector"
            )
            self.ping.start()
        self.listen_queue = None

    def listen(self, message_callback: Callable[[Dict], None]) -> None:
        self.listen_queue = ListenQueue(
            self.config, self.injector_config, self.injector_logger, message_callback
        )
        self.listen_queue.start()


class OpenAEVDetectionHelper:
    def __init__(self, logger, relevant_signatures_types) -> None:
        self.logger = logger
        self.relevant_signatures_types = relevant_signatures_types

    def match_alert_element_fuzzy(self, signature_value, alert_values, fuzzy_scoring):
        for alert_value in alert_values:
            self.logger.info(
                "Comparing alert value (" + alert_value + ", " + signature_value + ")"
            )
            ratio = fuzz.ratio(alert_value, signature_value)
            if ratio > fuzzy_scoring:
                self.logger.info("MATCHING! (score: " + str(ratio) + ")")
                return True
        return False

    def match_alert_elements(self, signatures, alert_data):
        return self._match_alert_elements_original(
            signatures, alert_data
        ) or self._match_alert_elements_for_command_line(signatures, alert_data)

    def _match_alert_elements_original(self, signatures, alert_data):
        # Example for alert_data
        # {"process_name": {"list": ["xx", "yy"], "fuzzy": 90}}
        relevant_signatures = [
            s for s in signatures if s["type"] in self.relevant_signatures_types
        ]

        # Matching logics
        signatures_number = len(relevant_signatures)
        matching_number = 0
        for signature in relevant_signatures:
            alert_data_for_signature = alert_data[signature["type"]]
            signature_result = False
            if alert_data_for_signature["type"] == "fuzzy":
                signature_result = self.match_alert_element_fuzzy(
                    signature["value"],
                    alert_data_for_signature["data"],
                    alert_data_for_signature["score"],
                )
            elif alert_data_for_signature["type"] == "simple":
                signature_result = signature["value"] in str(
                    alert_data_for_signature["data"]
                )

            if signature_result:
                matching_number = matching_number + 1

        if signatures_number == matching_number:
            return True
        return False

    def _match_alert_elements_for_command_line(self, signatures, alert_data):
        command_line_signatures = [
            signature
            for signature in signatures
            if signature.get("type") == "command_line"
        ]
        if len(command_line_signatures) == 0:
            return False
        key_types = ["command_line", "process_name", "file_name"]
        alert_datas = [alert_data.get(key) for key in key_types if key in alert_data]
        for signature in command_line_signatures:
            signature_result = False
            signature_value = self._decode_value(signature["value"]).strip().lower()
            for alert_data in alert_datas:
                trimmed_lowered_datas = [s.strip().lower() for s in alert_data["data"]]
                signature_result = any(
                    data in signature_value for data in trimmed_lowered_datas
                )
            if signature_result:
                return True
        return False

    def _decode_value(self, signature_value):
        if _is_base64_encoded(signature_value):
            try:
                decoded_bytes = base64.b64decode(signature_value)
                decoded_str = decoded_bytes.decode("utf-8")
                return decoded_str
            except Exception as e:
                self.logger.error(str(e))
        else:
            return signature_value


def _is_base64_encoded(str_maybe_base64):
    # Check if the length is a multiple of 4 and matches the Base64 character set
    base64_pattern = re.compile(r"^[A-Za-z0-9+/]*={0,2}$")
    return len(str_maybe_base64) % 4 == 0 and bool(
        base64_pattern.match(str_maybe_base64)
    )
