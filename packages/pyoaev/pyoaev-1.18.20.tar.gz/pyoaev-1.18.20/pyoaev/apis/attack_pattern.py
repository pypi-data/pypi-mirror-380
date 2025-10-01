from typing import Any, Dict, List

from pyoaev import exceptions as exc
from pyoaev.base import RESTManager, RESTObject


class AttackPattern(RESTObject):
    _id_attr = "attack_pattern_id"


class AttackPatternManager(RESTManager):
    _path = "/attack_patterns"
    _obj_cls = AttackPattern

    @exc.on_http_error(exc.OpenAEVUpdateError)
    def upsert(
        self,
        attack_patterns: List[Dict[str, Any]],
        ignore_dependencies: bool = False,
        **kwargs: Any,
    ) -> Dict[str, Any]:
        data = {
            "attack_patterns": attack_patterns,
            "ignore_dependencies": ignore_dependencies,
        }
        path = f"{self.path}/upsert"
        result = self.openaev.http_post(path, post_data=data, **kwargs)
        return result
