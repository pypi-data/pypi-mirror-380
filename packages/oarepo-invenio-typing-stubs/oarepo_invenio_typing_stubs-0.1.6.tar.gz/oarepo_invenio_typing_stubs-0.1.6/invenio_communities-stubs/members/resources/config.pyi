from typing import Any, ClassVar

import marshmallow as ma
from flask_resources import ResponseHandler
from invenio_communities.errors import CommunityDeletedError as CommunityDeletedError
from invenio_communities.members.errors import (
    AlreadyMemberError as AlreadyMemberError,
)
from invenio_communities.members.errors import (
    InvalidMemberError as InvalidMemberError,
)
from invenio_records_resources.resources import RecordResourceConfig

class MemberResourceConfig(RecordResourceConfig):
    url_prefix: ClassVar[str]
    routes: ClassVar[dict[str, str]]
    request_view_args: ClassVar[dict[str, ma.fields.Field]]
    # Mapping from exception type to an error handler (callable or factory)
    error_handlers: Any
    response_handlers: ClassVar[dict[str, ResponseHandler]]
