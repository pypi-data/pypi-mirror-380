from typing import Any, Optional, Type

from invenio_communities.records.records.systemfields.communities.context import (
    CommunitiesFieldContext as CommunitiesFieldContext,
)
from invenio_communities.records.records.systemfields.communities.manager import (
    CommunitiesRelationManager as CommunitiesRelationManager,
)
from invenio_records.api import Record
from invenio_records.systemfields import SystemField

class CommunitiesField(SystemField[Record, CommunitiesRelationManager]):
    def __init__(
        self,
        m2m_model_cls: Type[Any],
        key: str = "communities",
        context_cls: Optional[Type[Any]] = None,
        manager_cls: Optional[Type[Any]] = None,
    ) -> None: ...
    def pre_commit(self, record: Record) -> None: ...
    def obj(self, record: Record) -> CommunitiesRelationManager: ...
    def post_dump(
        self, record: Record, data: Any, dumper: Optional[Any] = None
    ) -> None: ...
    def post_load(
        self, record: Record, data: Any, loader: Optional[Any] = None
    ) -> None: ...
