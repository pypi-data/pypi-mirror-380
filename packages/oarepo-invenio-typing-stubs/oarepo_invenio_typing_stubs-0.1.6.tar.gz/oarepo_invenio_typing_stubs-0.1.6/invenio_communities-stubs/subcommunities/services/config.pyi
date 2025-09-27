from typing import Any, ClassVar, Collection

from invenio_communities.generators import CommunityOwners as CommunityOwners
from invenio_communities.subcommunities.services.request import (
    SubCommunityRequest as SubCommunityRequest,
)
from invenio_records_permissions.generators import Generator
from invenio_records_permissions.policies import BasePermissionPolicy
from invenio_records_resources.services.base.config import (
    ConfiguratorMixin,
    FromConfig,
    ServiceConfig,
)
from invenio_records_resources.services.base.results import ServiceItemResult

class SubCommunityPermissionPolicy(BasePermissionPolicy):
    can_request_join: ClassVar[Collection[Generator]]
    can_read: ClassVar[Collection[Generator]]
    can_create: ClassVar[Collection[Generator]]
    can_search: ClassVar[Collection[Generator]]
    can_update: ClassVar[Collection[Generator]]
    can_delete: ClassVar[Collection[Generator]]

class SubCommunityServiceConfig(ServiceConfig, ConfiguratorMixin):
    service_id = "subcommunities"
    permission_policy_cls = SubCommunityPermissionPolicy
    result_item_cls: type[ServiceItemResult]
    result_list_cls: Any
    schema: FromConfig
    request_cls: FromConfig
    links_item: dict[str, Any]
