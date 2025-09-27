from typing import Any, Callable, Type

from invenio_records.systemfields import SystemField
from invenio_records_resources.records.api import FileRecord, Record

# type: ignore[import-untyped]
from invenio_records_resources.records.systemfields.files.manager import FilesManager

class FilesField[R: Record = Record](SystemField[R, FilesManager]):
    _store: bool
    _dump: bool
    _dump_entries: bool | Callable[[R], bool]
    _enabled: bool
    _bucket_id_attr: str
    _bucket_attr: str
    _bucket_args: dict[str, Any]
    _create: bool
    _delete: bool
    _file_cls: type[FileRecord] | None
    def __init__(
        self,
        key: str = ...,
        bucket_id_attr: str = ...,
        bucket_attr: str = ...,
        store: bool = ...,
        dump: bool = ...,
        dump_entries: bool | Callable[[R], bool] = ...,
        file_cls: Type[FileRecord] | None = ...,
        enabled: bool = ...,
        bucket_args: dict[str, Any] | None = ...,
        create: bool = ...,
        delete: bool = ...,
    ): ...
    @property
    def _manager_options(self) -> dict[str, Any]: ...
    def dump(
        self, record: R, files: FilesManager, include_entries: bool = ...
    ) -> dict[str, Any]: ...
    @property
    def file_cls(self) -> Type[FileRecord] | None: ...
    def load(
        self,
        record: R,
        data: dict[str, Any],
        from_dump: bool = ...,
    ) -> FilesManager: ...
    def obj(self, record: R) -> FilesManager | None: ...
    def store(self, record: R, files: FilesManager): ...
