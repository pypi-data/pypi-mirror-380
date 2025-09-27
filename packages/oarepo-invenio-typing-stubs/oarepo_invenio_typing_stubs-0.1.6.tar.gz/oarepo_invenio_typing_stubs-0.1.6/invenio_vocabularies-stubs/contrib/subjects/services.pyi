from invenio_records_resources.services.records.config import RecordServiceConfig
from invenio_records_resources.services.records.service import RecordService
from invenio_vocabularies.contrib.subjects.subjects import record_type as record_type
from invenio_vocabularies.records.models import VocabularyScheme as VocabularyScheme

SubjectsServiceConfig: type[RecordServiceConfig]

class SubjectsService(RecordService):
    def create_scheme(
        self, identity, id_, name: str = "", uri: str = ""
    ) -> VocabularyScheme: ...
