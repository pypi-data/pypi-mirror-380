from invenio_records.systemfields import SystemField
from invenio_requests.customizations import RequestType as RequestType
from invenio_requests.proxies import (
    current_request_type_registry as current_request_type_registry,
)
from invenio_requests.records.api import Request

class RequestTypeField(SystemField[Request, RequestType]):
    def __init__(self, key: str = "type") -> None: ...
    def obj(self, instance: "Request") -> "RequestType": ...
    def set_obj(self, instance: "Request", obj: "RequestType") -> None: ...
