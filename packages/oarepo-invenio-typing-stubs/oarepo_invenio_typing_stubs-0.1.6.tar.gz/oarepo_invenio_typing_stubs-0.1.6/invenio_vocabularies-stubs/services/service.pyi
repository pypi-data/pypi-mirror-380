from typing import Any, Dict, List, Optional

from flask_principal import Identity
from invenio_db.uow import UnitOfWork
from invenio_records_resources.services import RecordService
from invenio_records_resources.services.records.results import RecordList
from invenio_search.engine import dsl
from invenio_vocabularies.records.models import VocabularyType as VocabularyType
from invenio_vocabularies.services.tasks import process_datastream as process_datastream

class VocabularyTypeService(RecordService):
    def rebuild_index(
        self, identity: Identity, uow: Optional[UnitOfWork] = None
    ) -> bool: ...
    def search(
        self,
        identity: Identity,
        params: Optional[Dict[str, Any]] = ...,
        search_preference: Optional[str] = ...,
        expand: bool = ...,
        **kwargs,
    ) -> RecordList: ...

class VocabulariesService(RecordService):
    @property
    def task_schema(self): ...
    def create_type(
        self,
        identity: Identity,
        id: str,
        pid_type: str,
        uow: Optional[UnitOfWork] = None,
    ) -> VocabularyType: ...
    def read_all(  # type: ignore[override]
        self,
        identity: Identity,
        fields: List[str],
        type: str,
        cache: bool = True,
        extra_filter: dsl.query.Query | str = "",
        **kwargs,
    ) -> RecordList: ...
    def read_many(
        self,
        identity: Identity,
        ids: List[str],
        fields: List[str] | None = None,
        **kwargs: Any,
    ) -> RecordList: ...
    def search(
        self,
        identity: Identity,
        params: Optional[Dict[str, Any]] = ...,
        search_preference: Optional[str] = ...,
        expand: bool = ...,
        **kwargs: Any,
    ) -> RecordList: ...
    def launch(self, identity: Identity, data: Dict[str, Any]) -> bool: ...
