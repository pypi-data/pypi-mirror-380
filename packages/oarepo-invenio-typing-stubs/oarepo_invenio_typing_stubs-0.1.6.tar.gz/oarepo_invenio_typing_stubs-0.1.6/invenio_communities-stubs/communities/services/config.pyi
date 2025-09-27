from typing import Any, ClassVar

from _typeshed import Incomplete
from invenio_communities.communities.records.api import Community as Community
from invenio_communities.communities.schema import (
    CommunityFeaturedSchema as CommunityFeaturedSchema,
)
from invenio_communities.communities.schema import CommunitySchema as CommunitySchema
from invenio_communities.communities.schema import TombstoneSchema as TombstoneSchema
from invenio_communities.communities.services import facets as facets
from invenio_communities.communities.services.components import (
    DefaultCommunityComponents as DefaultCommunityComponents,
)
from invenio_communities.communities.services.links import (
    CommunityEndpointLink as CommunityEndpointLink,
)
from invenio_communities.communities.services.links import (
    CommunityUIEndpointLink as CommunityUIEndpointLink,
)
from invenio_communities.communities.services.results import (
    CommunityFeaturedList as CommunityFeaturedList,
)
from invenio_communities.communities.services.results import (
    CommunityItem as CommunityItem,
)
from invenio_communities.communities.services.results import (
    CommunityListResult as CommunityListResult,
)
from invenio_communities.communities.services.results import (
    FeaturedCommunityItem as FeaturedCommunityItem,
)
from invenio_communities.communities.services.search_params import (
    IncludeDeletedCommunitiesParam as IncludeDeletedCommunitiesParam,
)
from invenio_communities.communities.services.search_params import (
    StatusParam as StatusParam,
)
from invenio_communities.communities.services.sort import (
    CommunitiesSortParam as CommunitiesSortParam,
)
from invenio_communities.permissions import (
    CommunityPermissionPolicy as CommunityPermissionPolicy,
)
from invenio_communities.permissions import (
    can_perform_action as can_perform_action,
)
from invenio_records_resources.services import FileServiceConfig
from invenio_records_resources.services.base.config import (
    ConfiguratorMixin,
    SearchOptionsMixin,
)
from invenio_records_resources.services.records.config import RecordServiceConfig
from invenio_records_resources.services.records.config import (
    SearchOptions as SearchOptionsBase,
)

class SearchOptions(SearchOptionsBase, SearchOptionsMixin):
    sort_featured: dict[str, Any]
    facets: ClassVar[dict[str, Any]]
    params_interpreters_cls: ClassVar[Any]

def children_allowed(record: Community | Incomplete, _: Any) -> bool: ...

class CommunityServiceConfig(RecordServiceConfig, ConfiguratorMixin):
    service_id = "communities"
    permission_policy_cls: Any
    record_cls = Community
    result_item_cls = CommunityItem
    result_list_cls = CommunityListResult
    indexer_queue_name: ClassVar[str]
    search: ClassVar[Any]
    schema: ClassVar[Any]
    schema_featured: Any = CommunityFeaturedSchema
    schema_tombstone: Any = TombstoneSchema
    result_list_cls_featured = CommunityFeaturedList
    result_item_cls_featured = FeaturedCommunityItem
    links_item: ClassVar[dict[str, Any]]
    action_link: ClassVar[Any]
    links_search: ClassVar[Any]
    links_featured_search: ClassVar[Any]
    links_user_search: ClassVar[Any]
    links_community_requests_search: ClassVar[Any]
    links_subcommunities_search: ClassVar[Any]
    available_actions: list[dict[str, str]]
    components: Any

class CommunityFileServiceConfig(FileServiceConfig, ConfiguratorMixin):
    record_cls = Community
    permission_policy_cls: Any
    file_links_item: ClassVar[dict[str, Any]]
