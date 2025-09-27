from typing import Any, ClassVar, Dict, List, Type

from invenio_records_resources.services import SearchOptions
from invenio_records_resources.services.records.components import (
    ServiceComponent as ServiceComponent,
)
from invenio_records_resources.services.records.facets import TermsFacet
from invenio_records_resources.services.records.params import QueryParser
from invenio_vocabularies.contrib.funders.facets import FundersLabels as FundersLabels
from werkzeug.local import LocalProxy

award_schemes: LocalProxy[Dict[str, Dict[str, Any]]]
awards_openaire_funders_mapping: LocalProxy[Dict[str, str]]
awards_ec_ror_id: LocalProxy[str]

class AwardsSearchOptions(SearchOptions):
    suggest_parser_cls: ClassVar[type[QueryParser] | None]
    facets: ClassVar[Dict[str, TermsFacet]]

service_components: List[Type[ServiceComponent]]
