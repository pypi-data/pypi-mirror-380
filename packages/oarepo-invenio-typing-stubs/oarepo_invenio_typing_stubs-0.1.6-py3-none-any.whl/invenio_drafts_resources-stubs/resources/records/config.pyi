from typing import ClassVar

from invenio_drafts_resources.resources.records.args import (
    SearchRequestArgsSchema as SearchRequestArgsSchema,
)
from invenio_records_resources.resources import (
    RecordResourceConfig as RecordResourceConfigBase,
)

class RecordResourceConfig(RecordResourceConfigBase):
    url_prefix: ClassVar[str]
    routes: ClassVar[dict[str, str]]
    request_search_args: ClassVar
