from typing import Any, ClassVar, Dict

from _typeshed import Incomplete
from invenio_records_resources.resources import (
    RecordResourceConfig,
    SearchRequestArgsSchema,
)
from invenio_records_resources.services.base.config import ConfiguratorMixin
from invenio_requests.errors import CannotExecuteActionError as CannotExecuteActionError
from invenio_requests.errors import NoSuchActionError as NoSuchActionError
from invenio_requests.resources.requests.fields import (
    ReferenceString as ReferenceString,
)
from marshmallow import fields

class RequestSearchRequestArgsSchema(SearchRequestArgsSchema):
    created_by: ReferenceString
    topic: ReferenceString
    receiver: ReferenceString
    is_open: fields.Boolean
    shared_with_me: fields.Boolean

request_error_handlers: Dict[type, Any]

class RequestsResourceConfig(RecordResourceConfig, ConfiguratorMixin):
    # Do not redeclare blueprint_name to avoid incompatible narrowing (base is None)
    # Match exact base types for overrides where needed
    url_prefix: ClassVar[str]
    routes: ClassVar[Dict[str, str]]
    request_view_args: ClassVar[Dict[str, Any]]
    request_search_args: ClassVar[type[SearchRequestArgsSchema]]
    error_handlers: ClassVar[Any]
    response_handlers: ClassVar[Dict[str, Incomplete]]
