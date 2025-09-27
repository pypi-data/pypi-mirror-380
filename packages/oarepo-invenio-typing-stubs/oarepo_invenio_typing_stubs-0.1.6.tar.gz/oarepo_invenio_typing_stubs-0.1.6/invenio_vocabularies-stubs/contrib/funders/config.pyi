from typing import Any, ClassVar, Dict, List, Type

from invenio_records_resources.services import SearchOptions
from invenio_records_resources.services.records.components import ServiceComponent
from invenio_records_resources.services.records.queryparser import QueryParser
from invenio_vocabularies.services.components import (
    ModelPIDComponent as ModelPIDComponent,
)
from werkzeug.local import LocalProxy

funder_schemes: LocalProxy[Dict[str, Dict[str, Any]]]
funder_fundref_doi_prefix: LocalProxy[str]
localized_title: LocalProxy[str]

class FundersSearchOptions(SearchOptions):
    suggest_parser_cls: ClassVar[type[QueryParser] | None]
    sort_default: ClassVar[str]
    sort_default_no_query: ClassVar[str]
    sort_options: ClassVar[Dict[str, Dict[str, Any]]]

service_components: List[Type[ServiceComponent]]
