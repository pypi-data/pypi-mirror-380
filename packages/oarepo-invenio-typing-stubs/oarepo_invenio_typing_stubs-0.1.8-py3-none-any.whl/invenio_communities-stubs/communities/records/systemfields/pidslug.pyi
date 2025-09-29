from typing import Any, Optional
from uuid import UUID

from invenio_communities.communities.records.api import Community
from invenio_records.systemfields import SystemField, SystemFieldContext
from invenio_records_resources.records.api import PersistentIdentifierWrapper

from oarepo_typing.descriptors import Descriptor

class PIDSlugFieldContext(SystemFieldContext):
    def parse_pid(self, value: Any) -> UUID | str: ...
    def resolve(self, pid_value: Any, registered_only: bool = True) -> Community: ...

class PIDSlugField(Descriptor[Community, Optional[PersistentIdentifierWrapper]], SystemField):  # type: ignore[misc]
    def __init__(self, id_field: str, slug_field: str) -> None: ...
    def obj(self, record: Community) -> Optional[PersistentIdentifierWrapper]: ...
    def pre_commit(self, record: Community) -> None: ...
