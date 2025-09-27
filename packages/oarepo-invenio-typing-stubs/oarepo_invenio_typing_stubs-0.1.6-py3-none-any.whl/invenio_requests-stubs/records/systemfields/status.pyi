from typing import Any, Optional, Type

from invenio_records.systemfields import SystemField
from invenio_requests.records.api import Request

class RequestStatusField(SystemField[Request, str]):
    def __get__(
        self, record: Optional[Any], owner: Optional[Type[Any]] = None
    ) -> Any: ...
    def __set__(self, record: "Request", value: str) -> None: ...
