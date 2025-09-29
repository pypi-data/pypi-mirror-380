from typing import (
    Any,
    Dict,
    Optional,
)

from invenio_records.api import Record
from invenio_records.systemfields.base import SystemField

from oarepo_typing.descriptors import Descriptor

class ConstantField[R: Record = Record, T = Any](Descriptor[R, T], SystemField):  # type: ignore[misc]
    value: T

    def __init__(
        self,
        key: Optional[str] = ...,
        value: T = ...,
    ): ...
    def pre_init(
        self, record: R, data: Optional[Dict[str, Any]], model: Any = ..., **kwargs: Any
    ) -> None: ...
