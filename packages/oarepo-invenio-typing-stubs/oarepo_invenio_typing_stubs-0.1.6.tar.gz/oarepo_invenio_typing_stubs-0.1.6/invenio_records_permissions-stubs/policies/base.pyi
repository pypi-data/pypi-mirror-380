from typing import Any, ClassVar, Collection, List, Set

from flask_principal import Need
from invenio_access import Permission
from invenio_records_permissions.generators import Generator
from invenio_search.engine import dsl

class BasePermissionPolicy(Permission):
    can_search: ClassVar[
        Collection[Generator]
    ]  # keep typing as Collection to allow tuples
    can_create: ClassVar[
        Collection[Generator]
    ]  # keep typing as Collection to allow tuples
    can_read: ClassVar[
        Collection[Generator]
    ]  # keep typing as Collection to allow tuples
    can_update: ClassVar[
        Collection[Generator]
    ]  # keep typing as Collection to allow tuples
    can_delete: ClassVar[
        Collection[Generator]
    ]  # keep typing as Collection to allow tuples
    action: str
    over: dict[str, Any]
    def __init__(self, action: str, **over: Any) -> None: ...
    @property
    def generators(self) -> List[Generator]: ...
    @property
    def needs(self) -> Set[Need]: ...
    @property
    def excludes(self) -> Set[Need]: ...
    def _query_filters_superuser(
        self, filters: List[dsl.query.Query]
    ) -> List[dsl.query.Query]: ...
    @property
    def query_filters(self) -> List[dsl.query.Query]: ...
