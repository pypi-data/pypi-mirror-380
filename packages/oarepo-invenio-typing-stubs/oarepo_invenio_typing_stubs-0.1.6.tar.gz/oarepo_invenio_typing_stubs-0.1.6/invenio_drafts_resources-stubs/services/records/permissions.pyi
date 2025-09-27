from typing import ClassVar, Collection

from invenio_records_permissions.generators import Generator
from invenio_records_permissions.policies.records import (
    RecordPermissionPolicy as RecordPermissionPolicyBase,
)

class RecordPermissionPolicy(RecordPermissionPolicyBase):
    can_create: ClassVar[Collection[Generator]]
    can_new_version: ClassVar[Collection[Generator]]
    can_edit: ClassVar[Collection[Generator]]
    can_publish: ClassVar[Collection[Generator]]
    can_read_draft: ClassVar[Collection[Generator]]
    can_update_draft: ClassVar[Collection[Generator]]
    can_delete_draft: ClassVar[Collection[Generator]]
    can_manage_files: ClassVar[Collection[Generator]]
