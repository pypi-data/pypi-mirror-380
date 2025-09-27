from typing import Any, Optional, Type

# type: ignore[import-untyped]
from invenio_pidstore.models import PersistentIdentifier

# type: ignore[import-untyped]
from invenio_pidstore.providers.recordid_v2 import RecordIdProviderV2
from invenio_pidstore.resolver import Resolver
from invenio_records.systemfields import (
    ModelField,
    RelatedModelField,
    RelatedModelFieldContext,
)
from invenio_records_resources.records.api import PersistentIdentifierWrapper, Record
from invenio_records_resources.records.providers import ModelPIDProvider
from invenio_records_resources.records.resolver import ModelResolver

class PIDFieldContext[R: Record = Record](RelatedModelFieldContext[R]):
    def resolve(
        self,
        pid_value: str,
        registered_only: bool = ...,
        with_deleted: bool = ...,
    ) -> R: ...

class PIDField[R: Record = Record, C: PIDFieldContext = PIDFieldContext[Record]](RelatedModelField[R, C, PersistentIdentifier]):  # type: ignore[type-var]
    def __init__(
        self,
        key: str = ...,
        provider: Optional[Type[RecordIdProviderV2]] = ...,
        pid_type: Optional[str] = ...,
        object_type: str = ...,
        resolver_cls: Optional[Type[Resolver]] = ...,
        delete: bool = ...,
        create: bool = ...,
        context_cls: Type[PIDFieldContext] = ...,
    ): ...
    def create(self, record: R) -> PersistentIdentifier: ...
    def delete(self, record: R) -> None: ...
    @staticmethod
    def dump_obj(field: Any, record: Any, pid: PersistentIdentifier): ...
    @staticmethod
    def load_obj(field: Any, record: Any) -> Optional[PersistentIdentifier]: ...
    def post_create(self, record: R): ...
    def post_delete(self, record: R, force: bool = ...): ...

class ModelPIDFieldContext[R: Record = Record](PIDFieldContext[R]):
    def resolve(
        self, pid_value: str, registered_only: bool = True, with_deleted: bool = ...
    ) -> R: ...
    def create(self, record: R) -> None: ...
    def session_merge(self, record: R) -> None: ...

class ModelPIDField[R: Record = Record](
    ModelField[R, Optional[PersistentIdentifierWrapper]]
):
    def __init__(
        self,
        model_field_name: str = ...,
        provider: Type[ModelPIDProvider] = ...,
        resolver_cls: Type[ModelResolver] = ...,
        context_cls: Type[ModelPIDFieldContext] = ...,
    ): ...
