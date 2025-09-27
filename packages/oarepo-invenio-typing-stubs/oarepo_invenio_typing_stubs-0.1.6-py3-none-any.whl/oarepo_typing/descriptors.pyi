from typing import Generic, Self, TypeVar, overload

T = TypeVar("T")  # owner type
V = TypeVar("V")  # value type

class Descriptor(Generic[T, V]):
    @overload
    def __get__(self, instance: None, owner: type[T]) -> Self: ...
    @overload
    def __get__(self, instance: T, owner: type[T]) -> V: ...
    @overload
    def __set__(self, instance: None, value: Self) -> None: ...
    @overload
    def __set__(self, instance: T, value: V) -> None: ...
