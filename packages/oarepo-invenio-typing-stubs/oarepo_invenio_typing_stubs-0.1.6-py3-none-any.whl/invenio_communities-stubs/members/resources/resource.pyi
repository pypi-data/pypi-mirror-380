from typing import Any

from invenio_records_resources.resources.records.resource import (
    RecordResource,
    request_data,
    request_extra_args,
    request_search_args,
    request_view_args,
)

class MemberResource(RecordResource):
    def create_url_rules(self) -> list[dict[str, Any]]: ...
    @request_view_args
    @request_search_args
    def search(self) -> tuple[dict[str, Any], int]: ...
    @request_view_args
    @request_search_args
    def search_public(self) -> tuple[dict[str, Any], int]: ...
    @request_view_args
    @request_search_args
    def search_invitations(self) -> tuple[dict[str, Any], int]: ...
    @request_view_args
    @request_data
    def add(self) -> tuple[str, int]: ...
    @request_view_args
    @request_data
    def invite(self) -> tuple[str, int]: ...
    @request_view_args
    @request_data
    def request_membership(self) -> tuple[dict[str, Any], int]: ...
    @request_view_args
    @request_extra_args
    @request_data
    def update(self) -> tuple[str, int]: ...
    @request_view_args
    @request_data
    def update_invitations(self) -> tuple[str, int]: ...
    @request_view_args
    @request_data
    def delete(self) -> tuple[str, int]: ...
