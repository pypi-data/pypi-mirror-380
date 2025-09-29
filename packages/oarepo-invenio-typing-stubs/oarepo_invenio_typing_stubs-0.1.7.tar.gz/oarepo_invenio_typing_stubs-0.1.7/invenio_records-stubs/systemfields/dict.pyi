from typing import Any, Optional

from invenio_records.api import Record
from invenio_records.systemfields.base import SystemField

class DictField[R: Record = Record](SystemField[R, dict[str, Any]]):
    clear_none: bool
    create_if_missing: bool

    def __init__(
        self,
        key: Optional[str] = ...,
        clear_none: bool = ...,
        create_if_missing: bool = ...,
    ): ...
