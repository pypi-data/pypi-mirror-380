from typing import Optional

from invenio_records_resources.records.api import Record
from invenio_records_resources.records.systemfields.calculated import CalculatedField
from invenio_requests.customizations.states import RequestState

class RequestStateCalculatedField(CalculatedField[Record, bool]):
    def __init__(
        self, key: Optional[str] = None, expected_state: RequestState = ...
    ) -> None: ...
    def calculate(self, record: Record) -> bool: ...
