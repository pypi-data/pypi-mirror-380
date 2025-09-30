from __future__ import annotations

from typing import Callable, Dict, Generic, TypeVar, Union, Iterable


T = TypeVar("T", bound=Callable)


class DontCache(Generic[T]):
    __slots__ = ("value",)
    value: T

    def __init__(self, value: T):
        self.value = value

    def unwrap(self) -> T:
        return self.value


Menu = Iterable[Dict]
MaybeNotCached = Union[T, DontCache[T]]
