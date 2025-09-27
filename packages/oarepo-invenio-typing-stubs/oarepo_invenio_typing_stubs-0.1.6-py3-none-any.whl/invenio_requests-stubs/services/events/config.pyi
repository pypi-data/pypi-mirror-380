from typing import Any, Dict

from invenio_records_resources.services import Link, RecordServiceConfig
from invenio_records_resources.services.base.config import ConfiguratorMixin
from invenio_records_resources.services.records.results import RecordItem, RecordList
from invenio_requests.records.api import Request as Request
from invenio_requests.records.api import RequestEvent as RequestEvent

class RequestEventItem(RecordItem):
    @property
    def id(self) -> str: ...

class RequestEventList(RecordList): ...

class RequestEventLink(Link):
    @staticmethod
    def vars(record: RequestEvent, vars: Dict[str, Any]) -> None: ...

class RequestEventsServiceConfig(RecordServiceConfig, ConfiguratorMixin):
    ...
