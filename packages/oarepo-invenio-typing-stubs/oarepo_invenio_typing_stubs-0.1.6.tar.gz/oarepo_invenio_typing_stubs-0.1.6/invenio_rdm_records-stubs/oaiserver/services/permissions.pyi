from typing import ClassVar, Collection

from invenio_records_permissions import BasePermissionPolicy
from invenio_records_permissions.generators import Generator

class OAIPMHServerPermissionPolicy(BasePermissionPolicy):
    can_read: ClassVar[Collection[Generator]]
    can_create: ClassVar[Collection[Generator]]
    can_delete: ClassVar[Collection[Generator]]
    can_update: ClassVar[Collection[Generator]]
    can_read_format: ClassVar[Collection[Generator]]
