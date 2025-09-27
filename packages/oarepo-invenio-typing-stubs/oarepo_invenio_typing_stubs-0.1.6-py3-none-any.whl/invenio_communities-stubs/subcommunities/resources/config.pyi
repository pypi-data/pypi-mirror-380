from typing import Any, ClassVar

import marshmallow as ma
from flask_resources import RequestBodyParser, ResourceConfig, ResponseHandler
from invenio_communities.communities.resources.args import (
    CommunitiesSearchRequestArgsSchema as CommunitiesSearchRequestArgsSchema,
)
from invenio_records_resources.services.base.config import ConfiguratorMixin

json_response_handler: ResponseHandler

class SubCommunityResourceConfig(ConfiguratorMixin, ResourceConfig):
    blueprint_name: ClassVar[str]
    url_prefix: ClassVar[str]
    routes: ClassVar[dict[str, str]]  # Route name to URL pattern mapping
    request_view_args: ClassVar[
        dict[str, ma.fields.Field]
    ]  # View argument field definitions
    request_read_args: ClassVar[dict[str, Any]]  # Read argument definitions
    request_extra_args: ClassVar[
        dict[str, ma.fields.Field]
    ]  # Extra argument definitions
    request_body_parsers: ClassVar[dict[str, RequestBodyParser]]  # Body parser mappings
    default_content_type: ClassVar[str]
    request_search_args: ClassVar[type[CommunitiesSearchRequestArgsSchema]]
    response_handlers: ClassVar[
        dict[str, ResponseHandler]
    ]  # Content type to handler mapping
    default_accept_mimetype: ClassVar[str]
    error_handlers: ClassVar[dict[type, Any]]  # Exception type to handler mapping
