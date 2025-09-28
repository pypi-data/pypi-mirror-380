from typing import Callable, Generic, TypeVar

import attrs
import cattrs

from apisix_client.common import ATTRS_META_APISIX_KEYWORD

converter = cattrs.GenConverter()


def get_apisix_unstructure_hook(cls) -> Callable[[object], dict]:
    def apisix_json_format(obj: object) -> dict:
        results = {}
        for field in attrs.fields(cls):
            field_data = getattr(obj, field.name)
            if not field_data and not isinstance(field_data, (int, float, bool)):
                continue

            key = field.metadata.get(ATTRS_META_APISIX_KEYWORD, field.name)
            results[key] = converter.unstructure(field_data)

        return results

    return apisix_json_format


converter.register_unstructure_hook_factory(
    lambda obj: hasattr(obj, "__attrs_attrs__"), get_apisix_unstructure_hook
)


V = TypeVar("V")


# https://apisix.apache.org/docs/apisix/admin-api/#v3-new-feature
@attrs.define()
class BaseResponse(Generic[V]):
    key: str = attrs.field(converter=str)
    created_index: int = attrs.field(converter=int)
    modified_index: int = attrs.field(converter=int)
    value: V = attrs.field()
