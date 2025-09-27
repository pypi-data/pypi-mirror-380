from typing import ClassVar, Collection

from invenio_records_permissions.generators import Generator as Generator
from invenio_vocabularies.services.generators import IfTags as IfTags
from invenio_vocabularies.services.permissions import (
    PermissionPolicy as PermissionPolicy,
)

class NamesPermissionPolicy(PermissionPolicy):
    can_search: ClassVar[Collection[Generator] | tuple[Generator, ...]]
    can_read: ClassVar[Collection[Generator] | tuple[Generator, ...]]
