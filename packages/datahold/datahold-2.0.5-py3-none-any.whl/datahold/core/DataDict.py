import collections
from typing import *

from frozendict import frozendict

from datahold._utils import deco
from datahold._utils.Cfg import Cfg
from datahold.core.DataABC import DataABC


@deco.funcDeco(
    funcnames=Cfg.cfg.data["datafuncs"]["Dict"],
    Frozen=frozendict,
    NonFrozen=dict,
)
@deco.initDeco(
    Frozen=frozendict,
    NonFrozen=dict,
)
class DataDict(DataABC, collections.abc.MutableMapping):
    __slots__ = ()
    data: frozendict
