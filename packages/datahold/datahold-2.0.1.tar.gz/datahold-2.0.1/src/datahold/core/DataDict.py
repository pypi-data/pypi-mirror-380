import collections
from typing import *

from frozendict import frozendict

from datahold._utils import deco
from datahold.core.DataABC import DataABC


@deco.funcDeco(
    "__contains__",
    "__delitem__",
    "__eq__",
    "__format__",
    "__ge__",
    "__getitem__",
    "__gt__",
    "__ior__",
    "__iter__",
    "__le__",
    "__len__",
    "__lt__",
    "__or__",
    "__repr__",
    "__reversed__",
    "__ror__",
    "__setitem__",
    "__str__",
    "clear",
    "copy",
    "get",
    "items",
    "keys",
    "pop",
    "popitem",
    "setdefault",
    "update",
    "values",
    Frozen=frozendict,
    NonFrozen=dict,
)
@deco.initDeco(
    Frozen=frozendict,
    NonFrozen=dict,
)
class DataDict(DataABC, collections.abc.MutableMapping):
    __slots__ = ()
