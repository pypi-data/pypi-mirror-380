import collections
from typing import *

from datahold._utils import deco
from datahold._utils.Cfg import Cfg
from datahold.core.DataABC import DataABC

__all__ = ["DataList"]


@deco.funcDeco(
    *Cfg.cfg.data["datafuncs"]["List"],
    Frozen=tuple,
    NonFrozen=list,
)
@deco.initDeco(
    Frozen=tuple,
    NonFrozen=list,
)
class DataList(DataABC, collections.abc.MutableSequence):
    __slots__ = ()
    data: tuple
