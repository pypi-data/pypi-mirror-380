import collections
from abc import ABCMeta, abstractmethod
from typing import *

import setdoc
from datarepr import datarepr
from scaevola import Scaevola

from datahold.core.HoldABC import HoldABC

__all__ = [
    "OkayABC",
]


class OkayABC(Scaevola, HoldABC):
    __slots__ = ()

    @setdoc.basic
    def __bool__(self: Self, /) -> bool:
        return bool(self._data)

    @setdoc.basic
    def __contains__(self: Self, other: Any, /) -> bool:
        return other in self._data

    @setdoc.basic
    def __eq__(self: Self, other: Any, /) -> bool:
        if type(self) is type(other):
            return self._data == other._data
        try:
            opp: Self = type(self)(other)
        except:
            return False
        else:
            return self._data == opp._data

    @setdoc.basic
    def __format__(self: Self, format_spec: Any = "", /) -> str:
        return format(self._data, str(format_spec))

    @setdoc.basic
    def __getitem__(self: Self, key: Any, /) -> Any:
        return self._data[key]

    @setdoc.basic
    def __gt__(self: Self, other: Any, /) -> bool:
        return not (self == other) and (self >= other)

    @setdoc.basic
    def __iter__(self: Self, /) -> Iterator:
        return iter(self._data)

    @setdoc.basic
    def __le__(self: Self, other: Any, /) -> bool:
        return self._data <= type(self._data)(other)

    @setdoc.basic
    def __len__(self: Self, /) -> int:
        return len(self._data)

    @setdoc.basic
    def __lt__(self: Self, other: Any, /) -> bool:
        return not (self == other) and (self <= other)

    @setdoc.basic
    def __ne__(self: Self, other: Any, /) -> bool:
        return not (self == other)

    @setdoc.basic
    def __repr__(self: Self, /) -> str:
        return datarepr(type(self).__name__, self._data)

    @setdoc.basic
    def __reversed__(self: Self, /) -> reversed:
        return reversed(self._data)

    @setdoc.basic
    def __str__(self: Self, /) -> str:
        return repr(self)

    @setdoc.basic
    def copy(self: Self, /) -> Self:
        return type(self)(self.data)
