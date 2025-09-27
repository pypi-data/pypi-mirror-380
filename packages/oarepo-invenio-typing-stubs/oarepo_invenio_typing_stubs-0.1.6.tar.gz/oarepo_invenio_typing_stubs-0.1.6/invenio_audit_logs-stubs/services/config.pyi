from typing import Any, ClassVar

from invenio_audit_logs.proxies import (
    current_audit_logs_actions_registry as current_audit_logs_actions_registry,
)
from invenio_audit_logs.records import AuditLog as AuditLog
from invenio_audit_logs.services import results as results
from invenio_audit_logs.services.permissions import (
    AuditLogPermissionPolicy as AuditLogPermissionPolicy,
)
from invenio_audit_logs.services.schema import AuditLogSchema as AuditLogSchema
from invenio_indexer.api import RecordIndexer
from invenio_records_resources.services.base import ServiceConfig
from invenio_records_resources.services.base.config import ConfiguratorMixin
from invenio_records_resources.services.base.results import (
    ServiceItemResult,
    ServiceListResult,
)
from invenio_records_resources.services.records.config import SearchOptions

class AuditLogSearchOptions(SearchOptions):
    sort_default: ClassVar[str]
    sort_default_no_query: ClassVar[str]
    query_parser_cls: ClassVar[Any]
    sort_options: ClassVar[dict[str, dict[str, Any]]]
    facets: ClassVar[dict[str, Any]]
    pagination_options: ClassVar[dict[str, int]]
    params_interpreters_cls: ClassVar[list[Any]]

def idvar(log, vars) -> None: ...

class AuditLogServiceConfig(ServiceConfig, ConfiguratorMixin):
    enabled: Any
    service_id: str | None
    permission_policy_cls: Any
    search: type[AuditLogSearchOptions]
    schema: type[AuditLogSchema]
    record_cls: type[AuditLog]
    indexer_cls: type[RecordIndexer]
    indexer_queue_name: str
    index_dumper: Any
    components: list[type]
    links_item: dict[str, Any]
    links_search: dict[str, Any]
    result_item_cls: type[ServiceItemResult]
    result_list_cls: type[ServiceListResult]
