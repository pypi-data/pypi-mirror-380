from typing import Any

from flask_resources import JSONSerializer as JSONSerializer
from flask_resources import ResponseHandler as ResponseHandler
from flask_resources import response_handler, with_content_negotiation
from invenio_drafts_resources.resources.records.errors import (
    RedirectException as RedirectException,
)
from invenio_records_resources.resources import RecordResource as RecordResourceBase
from invenio_records_resources.resources.records.headers import (
    etag_headers as etag_headers,
)
from invenio_records_resources.resources.records.resource import (
    request_data,
    request_extra_args,
    request_headers,
    request_read_args,
    request_search_args,
    request_view_args,
)

class RecordResource(RecordResourceBase):
    def create_blueprint(self, **options): ...
    def create_url_rules(self): ...
    @request_extra_args
    @request_search_args
    @request_view_args
    def search_user_records(self) -> tuple[dict[str, Any], int]: ...
    @request_extra_args
    @request_search_args
    @request_view_args
    def search_versions(self) -> tuple[dict[str, Any], int]: ...
    @request_extra_args
    @request_view_args
    def new_version(self) -> tuple[dict[str, Any], int]: ...
    @request_extra_args
    @request_view_args
    def edit(self) -> tuple[dict[str, Any], int]: ...
    @request_extra_args
    @request_view_args
    def publish(self) -> tuple[dict[str, Any], int]: ...
    @request_view_args
    @with_content_negotiation
    @response_handler(many=True)
    def import_files(self) -> tuple[dict[str, Any], int]: ...
    @request_extra_args
    @request_view_args
    def read_latest(self) -> None: ...
    @request_extra_args
    @request_read_args
    @request_view_args
    @response_handler()
    def read_draft(self) -> tuple[dict[str, Any], int]: ...
    @request_extra_args
    @request_headers
    @request_view_args
    @request_data
    @response_handler()
    def update_draft(self) -> tuple[dict[str, Any], int]: ...
    @request_headers
    @request_view_args
    def delete_draft(self) -> tuple[str, int]: ...
