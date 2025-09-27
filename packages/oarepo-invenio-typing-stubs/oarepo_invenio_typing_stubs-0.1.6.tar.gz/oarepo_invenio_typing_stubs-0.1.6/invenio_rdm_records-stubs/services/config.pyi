from typing import Any, ClassVar

from invenio_communities.communities.records.api import Community
from invenio_drafts_resources.services.records.config import (
    RecordServiceConfig,
    SearchDraftsOptions,
    SearchOptions,
    SearchVersionsOptions,
)
from invenio_rdm_records.services.customizations import (
    FromConfigConditionalPIDs,
    FromConfigPIDsProviders,
    FromConfigRequiredPIDs,
)
from invenio_rdm_records.services.result_items import (
    GrantItem,
    GrantList,
    SecretLinkItem,
    SecretLinkList,
)
from invenio_rdm_records.services.results import RDMRecordRevisionsList
from invenio_rdm_records.services.schemas.community_records import (
    CommunityRecordsSchema,
)
from invenio_rdm_records.services.schemas.parent.access import (
    AccessSettingsSchema,
    RequestAccessSchema,
)
from invenio_rdm_records.services.schemas.parent.access import (
    Grant as GrantSchema,
)
from invenio_rdm_records.services.schemas.parent.access import (
    Grants as GrantsSchema,
)
from invenio_rdm_records.services.schemas.parent.access import (
    SecretLink as SecretLinkSchema,
)
from invenio_rdm_records.services.schemas.quota import QuotaSchema
from invenio_rdm_records.services.schemas.tombstone import TombstoneSchema
from invenio_records_resources.services import (
    FileServiceConfig as BaseFileServiceConfig,
)
from invenio_records_resources.services.base.config import (
    ConfiguratorMixin,
    SearchOptionsMixin,
    ServiceConfig,
)
from invenio_records_resources.services.base.links import (
    ConditionalLink,
    EndpointLink,
    ExternalLink,
    NestedLinks,
)
from invenio_records_resources.services.records.config import (
    RecordServiceConfig as BaseRecordServiceConfig,
)

def is_draft_and_has_review(record, ctx): ...
def is_record_and_has_doi(record, ctx): ...
def is_record_or_draft_and_has_parent_doi(record, ctx): ...
def has_doi(record, ctx): ...
def is_iiif_compatible(file_, ctx): ...
def archive_download_enabled(record, ctx): ...
def _groups_enabled(record, ctx): ...
def is_datacite_test(record, ctx): ...
def lock_edit_published_files(service, identity, record=None, draft=None): ...
def has_image_files(record, ctx): ...
def record_thumbnail_sizes() -> list[int]: ...
def get_record_thumbnail_file(record, **kwargs) -> str | None: ...

class RDMSearchOptions(SearchOptions, SearchOptionsMixin):
    verified_sorting_enabled: ClassVar[bool]

class RDMCommunityRecordSearchOptions(RDMSearchOptions):
    verified_sorting_enabled: ClassVar[bool]

class RDMSearchDraftsOptions(SearchDraftsOptions, SearchOptionsMixin):
    facets: ClassVar[dict[str, Any]]
    params_interpreters_cls: ClassVar[list[type]]

class RDMSearchVersionsOptions(SearchVersionsOptions, SearchOptionsMixin):
    params_interpreters_cls: ClassVar[list[type]]

class RecordPIDLink(ExternalLink):
    def vars(self, record, vars: dict[str, Any]) -> None: ...

class ThumbnailLinks:
    link_for_thumbnail: EndpointLink
    def __init__(
        self, sizes: list[int] | None = None, when: Any | None = None
    ) -> None: ...
    def should_render(self, obj: Any, context: dict[str, Any]) -> bool: ...
    def expand(self, obj: Any, context: dict[str, Any]) -> dict[str, str]: ...

record_doi_link: ConditionalLink

def vars_preview_html(drafcord, vars: dict[str, Any]) -> None: ...
def get_pid_value(drafcord) -> str | None: ...
def is_record_or_draft(drafcord) -> str: ...
def get_iiif_uuid_of_drafcord_from_file_drafcord(
    file_drafcord, vars: dict[str, Any]
) -> str: ...
def get_iiif_uuid_of_file_drafcord(file_drafcord, vars: dict[str, Any]) -> str: ...
def get_iiif_uuid_of_drafcord(drafcord, vars: dict[str, Any]) -> str: ...
def vars_self_iiif(drafcord, vars: dict[str, Any]) -> None: ...

class WithFileLinks(type): ...

class FileServiceConfig(
    BaseFileServiceConfig, ConfiguratorMixin, metaclass=WithFileLinks
):
    name_of_file_blueprint: ClassVar[str]

class RDMFileRecordServiceConfig(FileServiceConfig, ConfiguratorMixin): ...

class RDMRecordServiceConfig(RecordServiceConfig, ConfiguratorMixin):
    schema_access_settings: ClassVar[type[AccessSettingsSchema]]
    schema_secret_link: ClassVar[type[SecretLinkSchema]]
    schema_grant: ClassVar[type[GrantSchema]]
    schema_grants: ClassVar[type[GrantsSchema]]
    schema_request_access: ClassVar[type[RequestAccessSchema]]
    schema_tombstone: ClassVar[type[TombstoneSchema]]
    schema_quota: ClassVar[type[QuotaSchema]]
    link_result_item_cls: ClassVar[type[SecretLinkItem]]
    link_result_list_cls: ClassVar[type[SecretLinkList]]
    grant_result_item_cls: ClassVar[type[GrantItem]]
    grant_result_list_cls: ClassVar[type[GrantList]]
    revision_result_list_cls: ClassVar[type[RDMRecordRevisionsList]]
    pids_providers: ClassVar[FromConfigPIDsProviders]
    pids_required: ClassVar[FromConfigRequiredPIDs]
    parent_pids_providers: ClassVar[FromConfigPIDsProviders]
    parent_pids_required: ClassVar[FromConfigRequiredPIDs]
    parent_pids_conditional: ClassVar[FromConfigConditionalPIDs]
    nested_links_item: ClassVar[list[NestedLinks]]
    record_file_processors: ClassVar[list[Any]]

class RDMCommunityRecordsConfig(BaseRecordServiceConfig, ConfiguratorMixin):
    community_cls: ClassVar[type[Community]]
    search_versions: ClassVar[type[RDMSearchVersionsOptions]]
    community_record_schema: ClassVar[type[CommunityRecordsSchema]]
    max_number_of_removals: ClassVar[int]
    links_search_community_records: ClassVar[dict[str, Any]]

class RDMRecordMediaFilesServiceConfig(RDMRecordServiceConfig): ...
class RDMMediaFileRecordServiceConfig(FileServiceConfig, ConfiguratorMixin): ...
class RDMFileDraftServiceConfig(FileServiceConfig, ConfiguratorMixin): ...
class RDMRecordCommunitiesConfig(ServiceConfig, ConfiguratorMixin): ...
class RDMRecordRequestsConfig(ServiceConfig, ConfiguratorMixin): ...
