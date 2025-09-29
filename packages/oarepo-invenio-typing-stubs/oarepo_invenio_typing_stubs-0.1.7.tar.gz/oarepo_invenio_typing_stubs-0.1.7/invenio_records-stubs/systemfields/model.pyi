from typing import Any, Optional

from invenio_records.api import Record
from invenio_records.systemfields.base import SystemField

class ModelField[R: Record = Record, T = Any](SystemField[R, T]):
    _model_field_name: Optional[str]
    dump: bool
    _dump_key: Optional[str]
    _dump_type: Optional[Any]

    def __init__(
        self,
        model_field_name: Optional[str] = ...,
        dump: bool = ...,
        dump_key: Optional[str] = ...,
        dump_type: Optional[Any] = ...,
        **kwargs: Any,
    ): ...
    def _set(self, model: Any, value: Any) -> None: ...
    @property
    def dump_key(self) -> str: ...
    @property
    def dump_type(self) -> Optional[Any]: ...
    @property
    def model_field_name(self) -> str: ...
    def post_init(
        self,
        record: R,
        data: dict[str, Any],
        model: Any | None = ...,
        **kwargs: Any,
    ) -> None: ...
