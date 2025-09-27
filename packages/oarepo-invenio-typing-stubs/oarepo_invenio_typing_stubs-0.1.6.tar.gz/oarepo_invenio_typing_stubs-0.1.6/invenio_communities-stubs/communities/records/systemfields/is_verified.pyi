from typing import Any, Optional

from invenio_communities.communities.records.api import Community
from invenio_records_resources.records.systemfields.calculated import (
    CalculatedIndexedField,
)

class IsVerifiedField(CalculatedIndexedField[Community, bool]):
    def __init__(self, key: Optional[str] = None, **kwargs: Any) -> None: ...
    def calculate(self, record: Community) -> bool: ...
