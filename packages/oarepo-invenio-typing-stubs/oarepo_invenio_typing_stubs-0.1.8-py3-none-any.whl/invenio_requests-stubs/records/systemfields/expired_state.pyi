from typing import Optional

from invenio_records_resources.records.api import Record
from invenio_records_resources.records.systemfields.calculated import CalculatedField

class ExpiredStateCalculatedField(CalculatedField[Record, bool]):
    def __init__(self, key: Optional[str] = None) -> None: ...
    def calculate(self, record: Record) -> bool: ...
