from typing import *

from frozendict import frozendict

from datahold._utils import deco
from datahold.core.DataDict import DataDict
from datahold.core.HoldABC import HoldABC

__all__ = [
    "HoldDict",
]


@deco.dataDeco()
class HoldDict(DataDict, HoldABC):
    __slots__ = ()
    data: frozendict
