from invenio_requests.ext import InvenioRequests
from invenio_requests.registry import TypeRegistry
from invenio_requests.resources import RequestsResource
from invenio_requests.services import (
    RequestEventsService,
    RequestsService,
    UserModerationRequestService,
)
from werkzeug.local import LocalProxy

current_requests: LocalProxy[InvenioRequests]
current_request_type_registry: LocalProxy[TypeRegistry]
current_event_type_registry: LocalProxy[TypeRegistry]
current_requests_service: LocalProxy[RequestsService]
current_events_service: LocalProxy[RequestEventsService]
current_requests_resource: LocalProxy[RequestsResource]
current_user_moderation_service: LocalProxy[UserModerationRequestService]
