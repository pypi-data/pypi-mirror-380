from typing import Any, List, Union

from invenio_pidstore.models import PIDStatus  # type: ignore[import-untyped]
from invenio_records.dumpers import Dumper
from invenio_records.systemfields import SystemField
from invenio_records_resources.records.api import Record

class PIDStatusCheckField[R: Record = Record](SystemField[R, bool]):
    _pid_status: List[PIDStatus]
    _dump: bool

    def __init__(
        self,
        key: str = ...,
        status: Union[PIDStatus, List[PIDStatus], None] = ...,
        dump: bool = ...,
    ) -> None: ...
    def pre_dump(
        self, record: R, data: dict[str, Any], dumper: Any | None = ...
    ) -> None: ...
    def pre_load(
        self, data: dict[str, Any], loader: Dumper | None = ..., **kwargs: Any
    ) -> None: ...
