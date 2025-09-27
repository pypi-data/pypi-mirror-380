from typing import Any, Callable, ClassVar

from invenio_drafts_resources.records.api import Draft
from invenio_drafts_resources.services.records.components import (
    DraftMetadataComponent as DraftMetadataComponent,
)
from invenio_drafts_resources.services.records.components import (
    PIDComponent as PIDComponent,
)
from invenio_drafts_resources.services.records.permissions import (
    RecordPermissionPolicy as RecordPermissionPolicy,
)
from invenio_drafts_resources.services.records.schema import (
    ParentSchema as ParentSchema,
)
from invenio_drafts_resources.services.records.schema import (
    RecordSchema as RecordSchema,
)
from invenio_drafts_resources.services.records.search_params import (
    AllVersionsParam as AllVersionsParam,
)
from invenio_indexer.api import RecordIndexer  # type: ignore[import-untyped]
from invenio_records_resources.services import (
    RecordServiceConfig as RecordServiceConfigBase,
)
from invenio_records_resources.services import SearchOptions as SearchOptionsBase

def is_draft(record, ctx): ...
def is_record(record, ctx): ...
def lock_edit_published_files(service, identity, record=None, draft=None): ...

class SearchOptions(SearchOptionsBase):
    sort_options: ClassVar[dict[str, dict[str, Any]]]
    params_interpreters_cls: ClassVar[list[type]]

class SearchDraftsOptions(SearchOptions):
    sort_default: ClassVar[str]
    sort_default_no_query: ClassVar[str]
    sort_options: ClassVar[dict[str, dict[str, Any]]]
    params_interpreters_cls: ClassVar[list[type]]

class SearchVersionsOptions(SearchOptions):
    sort_default: ClassVar[str]
    sort_default_no_query: ClassVar[str]
    sort_options: ClassVar[dict[str, dict[str, Any]]]
    facets_options: ClassVar[dict[str, Any]]
    params_interpreters_cls: ClassVar[list[type]]

class RecordServiceConfig(RecordServiceConfigBase):
    draft_cls: ClassVar[type[Draft] | None]
    draft_indexer_cls: ClassVar[type[RecordIndexer]]
    draft_indexer_queue_name: ClassVar[str]
    schema_parent: ClassVar[type[ParentSchema]]
    search: ClassVar
    search_drafts: ClassVar[type[SearchDraftsOptions]]
    search_versions: ClassVar[type[SearchVersionsOptions]]
    default_files_enabled: ClassVar[bool]
    default_media_files_enabled: ClassVar[bool]
    lock_edit_published_files: ClassVar[Callable[..., Any]]
    links_item: ClassVar[dict[str, Any]]
    links_search: ClassVar
    links_search_drafts: ClassVar
    links_search_versions: ClassVar
