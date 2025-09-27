from typing import Any, ClassVar

import marshmallow as ma
from flask_resources import ResourceConfig
from invenio_records_resources.resources.records.args import SearchRequestArgsSchema
from invenio_records_resources.services.base.config import ConfiguratorMixin

oaipmh_error_handlers: dict[type[BaseException], Any]

class OAIPMHServerSearchRequestArgsSchema(SearchRequestArgsSchema):
    managed: ClassVar[ma.fields.Boolean]
    sort_direction: ClassVar[ma.fields.Str]

class OAIPMHServerResourceConfig(ResourceConfig, ConfiguratorMixin):
    blueprint_name: ClassVar[str]
    url_prefix: ClassVar[str]
    routes: ClassVar[dict[str, str]]

    request_read_args: ClassVar[dict[str, Any]]
    request_view_args: ClassVar[dict[str, ma.fields.Field]]
    request_search_args: ClassVar[
        type[SearchRequestArgsSchema] | type[OAIPMHServerSearchRequestArgsSchema]
    ]

    error_handlers: ClassVar[dict[type[BaseException], Any]]

    response_handlers: ClassVar[dict[str, Any]]
