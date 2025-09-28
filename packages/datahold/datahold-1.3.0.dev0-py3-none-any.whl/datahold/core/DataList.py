import collections
from typing import *

from datahold._utils import deco
from datahold.core.DataABC import DataABC

__all__ = ["DataList"]


@deco.funcDeco(
    "__add__",
    "__contains__",
    "__delitem__",
    "__eq__",
    "__format__",
    "__ge__",
    "__getitem__",
    "__gt__",
    "__iadd__",
    "__imul__",
    "__iter__",
    "__le__",
    "__len__",
    "__lt__",
    "__mul__",
    "__repr__",
    "__reversed__",
    "__rmul__",
    "__setitem__",
    "__str__",
    "append",
    "clear",
    "copy",
    "count",
    "extend",
    "index",
    "insert",
    "pop",
    "remove",
    "reverse",
    "sort",
    Frozen=tuple,
    NonFrozen=list,
)
@deco.initDeco(
    Frozen=tuple,
    NonFrozen=list,
)
class DataList(DataABC, collections.abc.MutableSequence):
    __slots__ = ()
