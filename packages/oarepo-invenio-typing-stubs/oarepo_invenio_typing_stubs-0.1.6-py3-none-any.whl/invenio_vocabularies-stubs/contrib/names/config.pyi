from typing import Any, ClassVar, Dict, List, Type

from invenio_records_resources.services import SearchOptions
from invenio_records_resources.services.records.components import ServiceComponent
from invenio_records_resources.services.records.queryparser import QueryParser
from invenio_vocabularies.contrib.names.components import (
    InternalIDComponent as InternalIDComponent,
)
from invenio_vocabularies.services.components import PIDComponent as PIDComponent
from werkzeug.local import LocalProxy

names_schemes: LocalProxy[Dict[str, Dict[str, Any]]]

class NamesSearchOptions(SearchOptions):
    suggest_parser_cls: ClassVar[type[QueryParser] | None]
    sort_default: ClassVar[str]
    sort_default_no_query: ClassVar[str]
    sort_options: ClassVar[Dict[str, Dict[str, Any]]]

service_components: List[Type[ServiceComponent]]
