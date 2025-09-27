from typing import Any, ClassVar, Dict, List, Type

from invenio_records_resources.services import SearchOptions
from invenio_records_resources.services.records.components import ServiceComponent
from invenio_records_resources.services.records.queryparser import QueryParser
from invenio_vocabularies.services.components import PIDComponent as PIDComponent
from werkzeug.local import LocalProxy

affiliation_schemes: LocalProxy[Dict[str, Dict[str, Any]]]
affiliation_edmo_country_mappings: LocalProxy[Dict[str, str]]
localized_title: LocalProxy[str]

class AffiliationsSearchOptions(SearchOptions):
    suggest_parser_cls: ClassVar[type[QueryParser] | None]
    sort_default: ClassVar[str]
    sort_default_no_query: ClassVar[str]
    sort_options: ClassVar[Dict[str, Dict[str, Any]]]

service_components: List[Type[ServiceComponent]]
