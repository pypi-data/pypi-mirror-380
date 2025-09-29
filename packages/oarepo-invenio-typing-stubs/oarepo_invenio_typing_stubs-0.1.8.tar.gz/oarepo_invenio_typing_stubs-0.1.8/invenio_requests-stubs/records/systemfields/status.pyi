from typing import Any, Optional, Type

from invenio_records.systemfields import SystemField
from invenio_requests.records.api import Request

from oarepo_typing.descriptors import Descriptor

class RequestStatusField(Descriptor[Request, str], SystemField):  # type: ignore[misc]
    def __get__(
        self, record: Optional[Any], owner: Optional[Type[Any]] = None
    ) -> Any: ...
