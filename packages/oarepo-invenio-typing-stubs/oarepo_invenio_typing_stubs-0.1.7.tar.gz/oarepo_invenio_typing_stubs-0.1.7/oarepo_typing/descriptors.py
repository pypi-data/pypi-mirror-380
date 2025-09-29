from typing import Any, Self, overload


# only for type checking inside the .pyi file, not in runtime
class Descriptor[OWNER: Any = Any, CONTEXT: Any = Any]:
    @overload
    def __get__(self, instance: None, owner: type[OWNER]) -> Self: ...
    @overload
    def __get__(self, instance: OWNER, owner: type[OWNER]) -> CONTEXT: ...
    def __get__(self, instance: OWNER | None, owner: type[OWNER]) -> CONTEXT | Self: ...  # type: ignore
    def __set__(self, instance: OWNER, value: CONTEXT) -> None: ...


# descriptor with everything configurable
class GenericDescriptor[
    OWNER: Any = Any,
    CONTEXT: Any = Any,
    ON_CLASS_VALUE: Any = Any,
    SETTER_VALUE: Any = Any,
]:
    @overload
    def __get__(self, instance: None, owner: type[OWNER]) -> ON_CLASS_VALUE: ...
    @overload
    def __get__(self, instance: OWNER, owner: type[OWNER]) -> CONTEXT: ...
    def __get__(self, instance: OWNER | None, owner: type[OWNER]) -> CONTEXT | ON_CLASS_VALUE: ...  # type: ignore
    def __set__(self, instance: OWNER, value: SETTER_VALUE) -> None: ...
