from typing import Any, ClassVar, Optional, Type

from invenio_records_resources.services.base import ServiceConfig
from invenio_records_resources.services.files.processors import (
    FileProcessor,
)
from invenio_records_resources.services.files.results import FileItem, FileList
from invenio_records_resources.services.files.schema import FileSchema

class FileServiceConfig(ServiceConfig):
    record_cls: ClassVar[Optional[Type[Any]]]
    permission_action_prefix: ClassVar[str]

    file_result_item_cls: ClassVar[Type[FileItem]]
    file_result_list_cls: ClassVar[Type[FileList]]
    file_schema: ClassVar[Type[FileSchema]]

    max_files_count: ClassVar[int]

    file_links_list: ClassVar[dict[str, Any]]
    file_links_item: ClassVar[dict[str, Any]]

    allow_upload: ClassVar[bool]
    allow_archive_download: ClassVar[bool]

    file_processors: ClassVar[list[FileProcessor]]
