import collections
from typing import *

import setdoc
from frozendict import frozendict

from datahold.core.HoldDict import HoldDict
from datahold.core.OkayABC import OkayABC

__all__ = [
    "OkayDict",
]


class OkayDict(OkayABC, HoldDict):
    __slots__ = ()

    data: frozendict

    @setdoc.basic
    def __init__(self: Self, data: Iterable = (), /, **kwargs: Any) -> None:
        self.data = dict(data, **kwargs)

    @setdoc.basic
    def __or__(self: Self, other: Any, /) -> Self:
        return type(self)(self._data | dict(other))

    @classmethod
    def fromkeys(cls: type, iterable: Iterable, value: Any = None, /) -> Self:
        "This classmethod creates a new instance with keys from iterable and values set to value."
        return cls(dict.fromkeys(iterable, value))

    def get(self: Self, /, *args: Any) -> Any:
        "This method returns self[key] if key is in the dictionary, and default otherwise."
        return self._data.get(*args)

    def items(self: Self, /) -> collections.abc.ItemsView:
        "This method returns a view of the items of the current instance."
        return self._data.items()

    def keys(self: Self, /) -> collections.abc.KeysView:
        "This method returns a view of the keys of the current instance."
        return self._data.keys()

    def values(self: Self, /) -> collections.abc.ValuesView:
        "This method returns a view of the values of the current instance."
        return self._data.values()
