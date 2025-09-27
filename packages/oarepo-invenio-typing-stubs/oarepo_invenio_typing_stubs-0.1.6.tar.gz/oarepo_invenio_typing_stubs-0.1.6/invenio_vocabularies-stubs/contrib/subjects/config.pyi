from typing import Any, ClassVar, Dict, List, Type

from invenio_records_resources.services import SearchOptions
from invenio_records_resources.services.records.components import ServiceComponent
from invenio_records_resources.services.records.queryparser import QueryParser
from invenio_vocabularies.services.components import PIDComponent as PIDComponent
from werkzeug.local import LocalProxy

subject_schemes: LocalProxy[Dict[str, Dict[str, Any]]]
localized_title: LocalProxy[str]
gemet_file_url: LocalProxy[str]
euroscivoc_file_url: LocalProxy[str]
nvs_file_url: LocalProxy[str]

class SubjectsSearchOptions(SearchOptions):
    suggest_parser_cls: ClassVar[type[QueryParser] | None]
    sort_default: ClassVar[str]
    sort_default_no_query: ClassVar[str]
    sort_options: ClassVar[Dict[str, Dict[str, Any]]]

service_components: List[Type[ServiceComponent]]
