from typing import Any, Dict, Optional
from uuid import UUID

from invenio_communities.communities.records.api import Community
from invenio_records.systemfields import SystemField

from oarepo_typing.descriptors import Descriptor

def is_valid_uuid(value: Any) -> bool: ...

class ParentCommunityField(Descriptor[Community, Optional[Community]], SystemField):  # type: ignore[misc]
    def __init__(self, key: str = "parent") -> None: ...
    def obj(self, instance: Community) -> Optional[Community]: ...
    def set_obj(
        self, record: Community, obj: Community | UUID | str | None
    ) -> None: ...
    def post_dump(
        self, record: Community, data: Dict[str, Any], dumper: Optional[Any] = None
    ) -> None: ...
    def post_load(
        self, record: Community, data: Dict[str, Any], loader: Optional[Any] = None
    ) -> None: ...
