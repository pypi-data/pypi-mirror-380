from typing import Any, Dict, List

from flask_principal import Identity
from invenio_db.uow import UnitOfWork
from invenio_records_resources.services import RecordService
from invenio_records_resources.services.records.results import RecordList
from invenio_records_resources.services.records.schema import ServiceSchemaWrapper

class CommunityRecordsService(RecordService):
    @property
    def community_record_schema(self) -> ServiceSchemaWrapper: ...
    @property
    def community_cls(self): ...
    def search(  # type: ignore[override]
        self,
        identity: Identity,
        community_id: str,
        params: Dict[str, Any] | None = ...,
        search_preference: str | None = ...,
        extra_filter: Any | None = ...,
        scan: bool = ...,
        scan_params: Dict[str, Any] | None = ...,
        **kwargs: Any,
    ) -> RecordList: ...
    def _remove(
        self, community: Any, record: Any, identity: Identity
    ) -> List[Dict[str, Any]]: ...
    def delete(  # type: ignore[override]
        self,
        identity: Identity,
        community_id: str,
        data: Dict[str, Any],
        revision_id: int | None = ...,
        uow: UnitOfWork | None = None,
    ) -> List[Dict[str, Any]]: ...
