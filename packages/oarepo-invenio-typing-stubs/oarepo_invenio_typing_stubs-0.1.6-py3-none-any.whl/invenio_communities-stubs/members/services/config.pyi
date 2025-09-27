from typing import Any, ClassVar

from invenio_communities.communities.records.api import Community as Community
from invenio_communities.members.records import Member as Member
from invenio_communities.members.records.api import (
    ArchivedInvitation as ArchivedInvitation,
)
from invenio_communities.members.services import facets as facets
from invenio_communities.members.services.components import (
    CommunityMemberCachingComponent as CommunityMemberCachingComponent,
)
from invenio_communities.members.services.schemas import (
    MemberEntitySchema as MemberEntitySchema,
)
from invenio_records_resources.services import RecordServiceConfig, SearchOptions
from invenio_records_resources.services.base.config import ConfiguratorMixin

class PublicSearchOptions(SearchOptions):
    sort_default: ClassVar[str]
    sort_default_no_query: ClassVar[str]
    sort_options: ClassVar[dict[str, Any]]
    query_parser_cls: ClassVar[Any]

class InvitationsSearchOptions(SearchOptions):
    sort_default: ClassVar[str]
    sort_default_no_query: ClassVar[str]
    sort_options: ClassVar[dict[str, Any]]
    facets: ClassVar[dict[str, Any]]

class MemberSearchOptions(PublicSearchOptions):
    sort_default: ClassVar[str]
    sort_default_no_query: ClassVar[str]
    sort_options: ClassVar[dict[str, Any]]
    facets: ClassVar[dict[str, Any]]
    query_parser_cls: ClassVar[Any]

class MemberServiceConfig(RecordServiceConfig, ConfiguratorMixin):
    service_id = "members"
    community_cls = Community
    record_cls = Member
    schema: ClassVar[Any]
    indexer_queue_name: ClassVar[str]
    relations: ClassVar[dict[str, Any]]
    archive_cls = ArchivedInvitation
    archive_indexer_cls: ClassVar[Any]
    archive_indexer_queue_name: ClassVar[str]
    permission_policy_cls: Any
    search: ClassVar[Any]
    search_public: ClassVar[Any]
    search_invitations: ClassVar[Any]
    links_item: ClassVar[dict[str, Any]]
    links_search: ClassVar[Any]
    components: Any
