from __future__ import annotations

from flask_principal import Identity
from invenio_rdm_records.records.api import RDMRecord
from invenio_records_resources.services import FileService as _FileService

class RDMFileService(_FileService):
    def _check_record_deleted_permissions(
        self, record: RDMRecord, identity: Identity
    ) -> None: ...
    def _get_record(
        self, id_: str, identity: Identity, action: str, file_key: str | None = ...
    ) -> RDMRecord: ...
