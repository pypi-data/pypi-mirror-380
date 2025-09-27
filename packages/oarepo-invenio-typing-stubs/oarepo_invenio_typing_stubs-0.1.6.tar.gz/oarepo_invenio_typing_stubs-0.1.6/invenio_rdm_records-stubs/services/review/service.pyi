from __future__ import annotations

from typing import Any

from flask_principal import Identity
from invenio_db.uow import UnitOfWork
from invenio_drafts_resources.services.records import RecordService
from invenio_records_resources.services.records.results import RecordItem

class ReviewService(RecordService):
    @property
    def supported_types(self) -> list[str]: ...
    def _validate_request_type(self, request_type: str | None) -> Any: ...
    # Use variadics to avoid incompatible overrides with RecordService signatures
    def create(self, *args: Any, **kwargs: Any) -> RecordItem: ...
    def read(self, *args: Any, **kwargs: Any) -> Any: ...
    def update(self, *args: Any, **kwargs: Any) -> RecordItem: ...
    def delete(self, *args: Any, **kwargs: Any) -> bool: ...
    def submit(
        self,
        identity: Identity,
        id_: str,
        data: dict[str, Any] | None = ...,
        require_review: bool = ...,
        uow: UnitOfWork | None = ...,
    ) -> Any: ...
