from typing import TYPE_CHECKING, Any, Dict, Optional, Type, Union

from invenio_records.systemfields import SystemField
from invenio_requests.customizations import EventType as EventType
from invenio_requests.proxies import (
    current_event_type_registry as current_event_type_registry,
)

if TYPE_CHECKING:
    from invenio_records.models import RecordMetadataBase
    from invenio_requests.customizations.event_types import EventType
    from invenio_requests.records.api import RequestEvent

class EventTypeField(SystemField[RequestEvent, EventType]):
    def _set(
        self,
        model: "RecordMetadataBase",
        value: Union[str, "EventType", Type["EventType"]],
    ): ...
    @staticmethod
    def get_instance(
        value: Union[str, "EventType", Type["EventType"]],
    ) -> "EventType": ...
    def obj(self, instance: "RequestEvent") -> "EventType": ...
    def pre_init(
        self,
        record: "RequestEvent",
        data: Dict[str, Any],
        model: Optional["RecordMetadataBase"] = None,
        **kwargs: Any,
    ) -> None: ...
    def set_obj(self, instance: "RequestEvent", obj: "EventType") -> None: ...
