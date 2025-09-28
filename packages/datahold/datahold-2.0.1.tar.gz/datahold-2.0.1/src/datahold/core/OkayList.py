from typing import *

import setdoc

from datahold.core.HoldList import HoldList
from datahold.core.OkayABC import OkayABC

__all__ = [
    "OkayList",
]


class OkayList(OkayABC, HoldList):
    __slots__ = ()
    data: tuple

    @setdoc.basic
    def __add__(self: Self, other: Any, /) -> Self:
        return type(self)(self._data + list(other))

    @setdoc.basic
    def __init__(self: Self, data: Iterable = ()) -> None:
        self.data = data

    @setdoc.basic
    def __mul__(self: Self, value: SupportsIndex, /) -> Self:
        return type(self)(self.data * value)

    @setdoc.basic
    def __rmul__(self: Self, value: SupportsIndex, /) -> Self:
        return self * value

    def count(self: Self, value: Any, /) -> int:
        "This method returns the number of occurences of value."
        return self._data.count(value)

    def index(self: Self, /, *args: Any) -> int:
        "This method returns the index of the first occurence of value, or raises a ValueError if value is not present."
        return self._data.index(*args)
