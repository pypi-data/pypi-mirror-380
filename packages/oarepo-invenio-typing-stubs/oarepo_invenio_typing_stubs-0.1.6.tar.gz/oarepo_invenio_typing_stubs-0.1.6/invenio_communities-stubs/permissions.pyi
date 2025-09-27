from typing import ClassVar, Collection, Optional, TypedDict

from flask_principal import Identity
from invenio_communities.communities.records.api import Community
from invenio_communities.generators import AllowedMemberTypes as AllowedMemberTypes
from invenio_communities.generators import (
    AuthenticatedButNotCommunityMembers as AuthenticatedButNotCommunityMembers,
)
from invenio_communities.generators import CommunityCurators as CommunityCurators
from invenio_communities.generators import CommunityManagers as CommunityManagers
from invenio_communities.generators import (
    CommunityManagersForRole as CommunityManagersForRole,
)
from invenio_communities.generators import CommunityMembers as CommunityMembers
from invenio_communities.generators import CommunityOwners as CommunityOwners
from invenio_communities.generators import CommunitySelfMember as CommunitySelfMember
from invenio_communities.generators import IfCommunityDeleted as IfCommunityDeleted
from invenio_communities.generators import IfMemberPolicyClosed as IfMemberPolicyClosed
from invenio_communities.generators import (
    IfRecordSubmissionPolicyClosed as IfRecordSubmissionPolicyClosed,
)
from invenio_communities.generators import IfRestricted as IfRestricted
from invenio_communities.generators import ReviewPolicy as ReviewPolicy
from invenio_records_permissions.generators import Generator
from invenio_records_permissions.policies import BasePermissionPolicy

class CommunityPermissionPolicy(BasePermissionPolicy):
    """Permissions for Community CRUD operations."""

    can_create: ClassVar[Collection[Generator]]
    can_read: ClassVar[Collection[Generator]]
    can_read_deleted: ClassVar[Collection[Generator]]
    can_update: ClassVar[Collection[Generator]]
    can_delete: ClassVar[Collection[Generator]]
    can_purge: ClassVar[Collection[Generator]]
    can_manage_access: ClassVar[Collection[Generator]]
    can_create_restricted: ClassVar[Collection[Generator]]
    can_search: ClassVar[Collection[Generator]]
    can_search_user_communities: ClassVar[Collection[Generator]]
    can_search_invites: ClassVar[Collection[Generator]]
    can_search_requests: ClassVar[Collection[Generator]]
    can_rename: ClassVar[Collection[Generator]]
    can_submit_record: ClassVar[Collection[Generator]]
    can_include_directly: ClassVar[Collection[Generator]]
    can_members_add: ClassVar[Collection[Generator]]
    can_members_invite: ClassVar[Collection[Generator]]
    can_members_manage: ClassVar[Collection[Generator]]
    can_members_search: ClassVar[Collection[Generator]]
    can_members_search_public: ClassVar[Collection[Generator]]
    can_members_bulk_update: ClassVar[Collection[Generator]]
    can_members_bulk_delete = can_members_bulk_update
    can_members_update: ClassVar[Collection[Generator]]
    can_members_delete = can_members_update
    can_invite_owners: ClassVar[Collection[Generator]]
    can_featured_search: ClassVar[Collection[Generator]]
    can_featured_list: ClassVar[Collection[Generator]]
    can_featured_create: ClassVar[Collection[Generator]]
    can_featured_update: ClassVar[Collection[Generator]]
    can_featured_delete: ClassVar[Collection[Generator]]
    can_moderate: ClassVar[Collection[Generator]]
    can_set_theme: ClassVar[Collection[Generator]]
    can_delete_theme = can_set_theme
    can_manage_children: ClassVar[Collection[Generator]]
    can_manage_parent: ClassVar[Collection[Generator]]
    can_request_membership: ClassVar[Collection[Generator]]

class PermissionContext(TypedDict, total=False):
    action: str
    identity: Optional[Identity]
    permission_policy_cls: type[BasePermissionPolicy]

def can_perform_action(community: Community, context: PermissionContext) -> bool: ...
