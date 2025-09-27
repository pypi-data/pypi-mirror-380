from __future__ import annotations

from typing import Any

from flask_principal import Identity
from invenio_records_resources.services import Service
from invenio_records_resources.services.records.results import RecordList

class RecordRequestsService(Service):
    @property
    def record_cls(self) -> Any: ...
    def search(
        self,
        identity: Identity,
        record_pid: str,
        params: dict[str, Any] | None = ...,
        search_preference: str | None = ...,
        expand: bool = ...,
        extra_filter: Any | None = ...,
        **kwargs: Any,
    ) -> RecordList: ...
