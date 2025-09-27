from typing import Any, ClassVar

import marshmallow as ma
from flask_resources import ResponseHandler
from invenio_communities.communities.resources.args import (
    CommunitiesSearchRequestArgsSchema as CommunitiesSearchRequestArgsSchema,
)
from invenio_communities.communities.resources.serializer import (
    UICommunityJSONSerializer as UICommunityJSONSerializer,
)
from invenio_communities.errors import CommunityDeletedError as CommunityDeletedError
from invenio_communities.errors import (
    CommunityFeaturedEntryDoesNotExistError as CommunityFeaturedEntryDoesNotExistError,
)
from invenio_communities.errors import LogoNotFoundError as LogoNotFoundError
from invenio_communities.errors import LogoSizeLimitError as LogoSizeLimitError
from invenio_communities.errors import (
    OpenRequestsForCommunityDeletionError as OpenRequestsForCommunityDeletionError,
)
from invenio_communities.errors import (
    SetDefaultCommunityError as SetDefaultCommunityError,
)
from invenio_records_resources.resources import (
    RecordResourceConfig,
    SearchRequestArgsSchema,
)
from invenio_records_resources.services.base.config import ConfiguratorMixin
from invenio_requests.resources.requests.config import RequestSearchRequestArgsSchema

community_error_handlers: dict[type, Any]

class CommunityResourceConfig(RecordResourceConfig, ConfiguratorMixin):
    url_prefix: ClassVar[str]
    routes: ClassVar[dict[str, str]]
    request_search_args: ClassVar[type[SearchRequestArgsSchema]]
    request_view_args: ClassVar[dict[str, ma.fields.Field]]
    error_handlers: Any
    request_community_requests_search_args: ClassVar[
        type[RequestSearchRequestArgsSchema]
    ]
    response_handlers: ClassVar[dict[str, ResponseHandler]]
