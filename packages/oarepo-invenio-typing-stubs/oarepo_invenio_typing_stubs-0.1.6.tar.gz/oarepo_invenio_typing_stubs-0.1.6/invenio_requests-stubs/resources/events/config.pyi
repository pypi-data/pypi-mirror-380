from typing import Any, ClassVar, Dict

from invenio_records_resources.resources import RecordResourceConfig

class RequestCommentsResourceConfig(RecordResourceConfig):
    blueprint_name: ClassVar[None]
    url_prefix: ClassVar[str]
    routes: ClassVar[Dict[str, str]]
    request_list_view_args: ClassVar[Dict[str, Any]]
    request_item_view_args: ClassVar[Dict[str, Any]]
    response_handlers: ClassVar[Dict[str, Any]]
