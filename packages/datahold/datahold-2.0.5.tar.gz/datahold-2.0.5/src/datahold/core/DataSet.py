import collections
from typing import *

from datahold._utils import deco
from datahold._utils.Cfg import Cfg
from datahold.core.DataABC import DataABC

__all__ = ["DataSet"]


@deco.funcDeco(
    funcnames=Cfg.cfg.data["datafuncs"]["Set"],
    Frozen=frozenset,
    NonFrozen=set,
)
@deco.initDeco(
    Frozen=frozenset,
    NonFrozen=set,
)
class DataSet(DataABC, collections.abc.MutableSet):
    __slots__ = ()
    data: frozenset
