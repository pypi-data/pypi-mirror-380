from typing import Any, Dict

from invenio_audit_logs.services import AuditLogService
from werkzeug.local import LocalProxy

current_audit_logs_service: LocalProxy[AuditLogService]
current_audit_logs_actions_registry: LocalProxy[Dict[str, Any]]
current_audit_logs_resolvers: LocalProxy[Any]
