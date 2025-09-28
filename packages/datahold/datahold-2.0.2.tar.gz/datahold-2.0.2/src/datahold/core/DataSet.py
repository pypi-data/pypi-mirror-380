import collections
from typing import *

from datahold._utils import deco
from datahold.core.DataABC import DataABC

__all__ = ["DataSet"]


@deco.funcDeco(
    "__and__",
    "__contains__",
    "__eq__",
    "__format__",
    "__ge__",
    "__gt__",
    "__iand__",
    "__ior__",
    "__isub__",
    "__iter__",
    "__ixor__",
    "__le__",
    "__len__",
    "__lt__",
    "__or__",
    "__rand__",
    "__repr__",
    "__ror__",
    "__rsub__",
    "__rxor__",
    "__str__",
    "__sub__",
    "__xor__",
    "add",
    "clear",
    "copy",
    "difference",
    "difference_update",
    "discard",
    "intersection",
    "intersection_update",
    "isdisjoint",
    "issubset",
    "issuperset",
    "pop",
    "remove",
    "symmetric_difference",
    "symmetric_difference_update",
    "union",
    "update",
    Frozen=frozenset,
    NonFrozen=set,
)
@deco.initDeco(
    Frozen=frozenset,
    NonFrozen=set,
)
class DataSet(DataABC, collections.abc.MutableSet):
    __slots__ = ()
