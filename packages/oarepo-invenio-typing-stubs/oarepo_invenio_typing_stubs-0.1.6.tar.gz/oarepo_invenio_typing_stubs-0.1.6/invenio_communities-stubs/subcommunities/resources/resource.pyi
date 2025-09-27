from typing import Any, Dict, List, Tuple

from flask_resources import Resource, response_handler
from invenio_records_resources.resources.records.resource import (
    request_data,
    request_view_args,
)

class SubCommunityResource(Resource):
    service: Any
    def __init__(self, config, service) -> None: ...
    def create_url_rules(self) -> List[Dict[str, Any]]: ...
    @request_view_args
    @response_handler()
    @request_data
    def join(self) -> Tuple[Dict[str, Any], int]: ...
