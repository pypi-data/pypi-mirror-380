from typing import (
    Any,
    Dict,
    Optional,
)

from invenio_records.api import Record
from invenio_records.systemfields.base import SystemField

class ConstantField[R: Record = Record, T = Any](SystemField[R, T]):
    value: T

    def __init__(
        self,
        key: Optional[str] = ...,
        value: T = ...,
    ): ...
    def pre_init(
        self, record: R, data: Optional[Dict[str, Any]], model: Any = ..., **kwargs: Any
    ) -> None: ...
