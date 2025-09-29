from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Iterable, Iterator, Optional

from _typeshed import Incomplete
from invenio_records_resources.pagination import Pagination
from invenio_records_resources.records.api import Record
from invenio_records_resources.services.base import Service
from invenio_records_resources.services.base.links import Link, LinksTemplate
from invenio_records_resources.services.base.results import (
    ServiceBulkItemResult,
    ServiceBulkListResult,
    ServiceItemResult,
    ServiceListResult,
)
from invenio_records_resources.services.records.schema import ServiceSchemaWrapper
from invenio_records_resources.services.records.service import RecordService

class ExpandableField(ABC):
    def __init__(self, field_name: str): ...
    @property
    def field_name(self) -> str: ...
    @abstractmethod
    def get_value_service(self, value: Incomplete) -> Incomplete: ...
    @abstractmethod
    def ghost_record(self, value: Incomplete) -> Incomplete: ...
    @abstractmethod
    def system_record(self) -> Incomplete: ...
    def has(self, service: Service, value: Incomplete) -> bool: ...
    def add_service_value(self, service: Service, value: Incomplete) -> None: ...
    def add_dereferenced_record(
        self, service: Service, value: Incomplete, resolved_rec: Incomplete
    ) -> None: ...
    def get_dereferenced_record(
        self, service: Service, value: Incomplete
    ) -> Incomplete: ...
    @abstractmethod
    def pick(self, identity: Incomplete, resolved_rec: Incomplete) -> Incomplete: ...

class FieldsResolver:
    def __init__(self, expandable_fields: Optional[list[ExpandableField]]): ...
    def resolve(
        self,
        identity: Incomplete,
        hits: Iterable[dict[str, Incomplete]],
    ) -> None: ...
    def expand(
        self,
        identity: Incomplete,
        hit: dict[str, Incomplete],
    ) -> dict[str, Incomplete]: ...

class MultiFieldsResolver(FieldsResolver):
    def expand(
        self, identity: Incomplete, hit: dict[str, Incomplete]
    ) -> dict[str, Incomplete]: ...

class RecordBulkItem(ServiceBulkItemResult):
    def __init__(
        self,
        op_type: str,
        record: Record,
        errors: Optional[list[Incomplete]],
        exc: Optional[BaseException],
    ): ...
    @property
    def errors(self) -> Optional[list[Incomplete]]: ...
    @property
    def op_type(self) -> str: ...
    @property
    def record(
        self,
    ) -> Record: ...
    @property
    def exc(self) -> Optional[BaseException]: ...

class RecordBulkList(ServiceBulkListResult):
    def __init__(
        self, service: Service, identity: Incomplete, results: list[Incomplete]
    ): ...
    @property
    def results(self) -> Iterator[RecordBulkItem]: ...

class RecordItem(ServiceItemResult):
    _service: RecordService  # keep typing
    _identity: Incomplete  # keep typing
    _record: Record  # keep typing
    _errors: Optional[list[Incomplete]]  # keep typing
    _links_tpl: Optional[LinksTemplate]  # keep typing
    _schema: ServiceSchemaWrapper  # keep typing
    _expandable_fields: Optional[list[ExpandableField]]  # keep typing
    _expand: bool  # keep typing
    _nested_links_item: Optional[list[Link]]  # keep typing
    _data: Optional[dict[str, Incomplete]]  # keep typing

    def __getitem__(self, key: str) -> Incomplete: ...
    def __init__(
        self,
        service: Service,
        identity: Incomplete,
        record: Record,
        errors: Optional[list[Incomplete]] = ...,
        links_tpl: Optional[LinksTemplate] = ...,
        schema: Optional[ServiceSchemaWrapper] = ...,
        expandable_fields: Optional[list[ExpandableField]] = ...,
        expand: bool = ...,
        nested_links_item: Optional[list[Link]] = ...,
    ): ...
    @property
    def _obj(self) -> Record: ...
    @property
    def data(self) -> dict[str, Incomplete]: ...
    def has_permissions_to(self, actions: list[str]) -> dict[str, bool]: ...
    @property
    def id(self) -> str: ...
    @property
    def links(self) -> dict[str, Incomplete]: ...
    @property
    def errors(self) -> Optional[list[Incomplete]]: ...
    def to_dict(self) -> dict[str, Incomplete]: ...

class RecordList(ServiceListResult):
    _expand: bool  # keep typing
    _identity: Incomplete  # keep typing
    _fields_resolver: Optional[FieldsResolver]  # keep typing
    _schema: ServiceSchemaWrapper  # keep typing
    _expandable_fields: Optional[list[ExpandableField]]  # keep typing
    _links_tpl: Optional[LinksTemplate]  # keep typing
    _links_item_tpl: Optional[LinksTemplate]  # keep typing
    _nested_links_item: Optional[list[Link]]  # keep typing
    _service: RecordService  # keep typing
    _results: Incomplete  # keep typing

    def __init__(
        self,
        service: RecordService,
        identity: Incomplete,
        results: Incomplete,
        params: Optional[dict[str, Incomplete]] = ...,
        links_tpl: Optional[LinksTemplate] = ...,
        links_item_tpl: Optional[LinksTemplate] = ...,
        nested_links_item: Optional[list[Link]] = ...,
        schema: Optional[ServiceSchemaWrapper] = ...,
        expandable_fields: Optional[list[ExpandableField]] = ...,
        expand: bool = ...,
    ): ...
    def __iter__(self) -> Iterator[dict[str, Incomplete]]: ...
    def __len__(self) -> int: ...
    @property
    def aggregations(self) -> Optional[dict[str, Incomplete]]: ...
    @property
    def hits(self) -> Iterator[dict[str, Incomplete]]: ...
    @property
    def pagination(self) -> Pagination: ...
    def to_dict(self) -> dict[str, Incomplete]: ...
    @property
    def total(self) -> Optional[int]: ...
