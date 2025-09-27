from typing import Any, Dict, Tuple

from invenio_records_resources.resources import RecordResource
from invenio_records_resources.resources.records.resource import (
    request_extra_args,
    request_headers,
)
from invenio_requests.customizations.event_types import (
    CommentEventType as CommentEventType,
)

class RequestCommentsResource(RecordResource):
    list_view_args_parser: Any
    item_view_args_parser: Any
    search_args_parser: Any
    data_parser: Any
    def create_url_rules(self): ...
    @list_view_args_parser
    @request_extra_args
    @data_parser
    def create(self) -> Tuple[Dict[str, Any], int]: ...
    @item_view_args_parser
    @request_extra_args
    def read(self) -> Tuple[Dict[str, Any], int]: ...
    @item_view_args_parser
    @request_extra_args
    @request_headers
    @data_parser
    def update(self) -> Tuple[Dict[str, Any], int]: ...
    @item_view_args_parser
    @request_headers
    def delete(self): ...
    @list_view_args_parser
    @request_extra_args
    @search_args_parser
    def search(self) -> Tuple[Dict[str, Any], int]: ...
