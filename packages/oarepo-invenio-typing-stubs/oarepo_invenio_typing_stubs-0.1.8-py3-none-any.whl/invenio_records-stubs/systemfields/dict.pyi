from typing import Any, Optional

from invenio_records.api import Record
from invenio_records.systemfields.base import SystemField

from oarepo_typing.descriptors import Descriptor

class DictField[R: Record = Record](Descriptor[R, dict[str, Any]], SystemField):  # type: ignore[misc]
    clear_none: bool
    create_if_missing: bool

    def __init__(
        self,
        key: Optional[str] = ...,
        clear_none: bool = ...,
        create_if_missing: bool = ...,
    ): ...
