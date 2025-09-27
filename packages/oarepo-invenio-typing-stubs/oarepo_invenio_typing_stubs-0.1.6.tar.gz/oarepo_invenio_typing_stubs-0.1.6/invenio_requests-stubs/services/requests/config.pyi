from typing import Any, Callable, ClassVar, Dict

from invenio_records_resources.services import RecordServiceConfig, SearchOptions
from invenio_records_resources.services.base.config import (
    ConfiguratorMixin,
    SearchOptionsMixin,
)
from invenio_requests.customizations import RequestActions as RequestActions
from invenio_requests.records.api import Request as Request
from invenio_requests.services.permissions import PermissionPolicy as PermissionPolicy
from invenio_requests.services.requests import facets as facets
from invenio_requests.services.requests.components import (
    EntityReferencesComponent as EntityReferencesComponent,
)
from invenio_requests.services.requests.components import (
    RequestDataComponent as RequestDataComponent,
)
from invenio_requests.services.requests.components import (
    RequestNumberComponent as RequestNumberComponent,
)
from invenio_requests.services.requests.components import (
    RequestPayloadComponent as RequestPayloadComponent,
)
from invenio_requests.services.requests.components import (
    RequestReviewersComponent as RequestReviewersComponent,
)
from invenio_requests.services.requests.links import RequestLink as RequestLink
from invenio_requests.services.requests.params import IsOpenParam as IsOpenParam
from invenio_requests.services.requests.params import (
    ReferenceFilterParam as ReferenceFilterParam,
)
from invenio_requests.services.requests.params import (
    SharedOrMyRequestsParam as SharedOrMyRequestsParam,
)
from invenio_requests.services.requests.results import RequestItem as RequestItem
from invenio_requests.services.requests.results import RequestList as RequestList

def _is_action_available(request: Request, context: Dict[str, Any]) -> bool: ...

class RequestSearchOptions(SearchOptions, SearchOptionsMixin):
    facets: ClassVar[Dict[str, Any]]

class UserRequestSearchOptions(RequestSearchOptions): ...

class RequestsServiceConfig(RecordServiceConfig, ConfiguratorMixin):
    # Only declare attributes that don't conflict with base invariants here
    search_user_requests: ClassVar[type[UserRequestSearchOptions]]
    links_user_requests_search: ClassVar[Dict[str, Callable[..., Any]]]
    action_link: ClassVar[Any]
    payload_schema_cls: ClassVar[type]
