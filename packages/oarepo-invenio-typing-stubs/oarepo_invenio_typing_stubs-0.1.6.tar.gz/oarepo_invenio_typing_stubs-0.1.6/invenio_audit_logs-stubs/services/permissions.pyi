from typing import ClassVar, Collection

from invenio_records_permissions.generators import Generator
from invenio_records_permissions.policies import BasePermissionPolicy

class AuditLogPermissionPolicy(BasePermissionPolicy):
    can_search: ClassVar[Collection[Generator]]
    can_create: ClassVar[Collection[Generator]]
    can_read: ClassVar[Collection[Generator]]
    can_update: ClassVar[Collection[Generator]]
    can_delete: ClassVar[Collection[Generator]]
