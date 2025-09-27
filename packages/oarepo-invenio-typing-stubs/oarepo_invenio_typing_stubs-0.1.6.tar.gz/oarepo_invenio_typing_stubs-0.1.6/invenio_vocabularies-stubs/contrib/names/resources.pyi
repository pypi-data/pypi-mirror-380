from typing import Any, ClassVar

from invenio_records_resources.resources.records.config import RecordResourceConfig
from invenio_records_resources.resources.records.resource import (
    RecordResource,
    request_view_args,
)
from marshmallow import fields

class NamesResourceConfig(RecordResourceConfig):
    routes: ClassVar[dict[str, str]]
    request_view_args: ClassVar[dict[str, fields.Field]]

class NamesResource(RecordResource):
    def create_url_rules(self) -> list[Any]: ...
    @request_view_args
    def name_resolve_by_id(self): ...
