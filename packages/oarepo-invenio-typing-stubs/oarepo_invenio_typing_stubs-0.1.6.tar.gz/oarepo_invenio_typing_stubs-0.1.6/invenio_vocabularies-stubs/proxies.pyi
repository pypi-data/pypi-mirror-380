from invenio_vocabularies.resources import VocabulariesResource as VocabulariesResource
from invenio_vocabularies.services.service import (
    VocabulariesService as VocabulariesService,
)
from werkzeug.local import LocalProxy

current_service: LocalProxy[VocabulariesService]
current_resource: LocalProxy[VocabulariesResource]
