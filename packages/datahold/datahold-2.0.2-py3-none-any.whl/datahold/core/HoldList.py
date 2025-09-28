from typing import *

from datahold._utils import deco
from datahold.core.DataList import DataList
from datahold.core.HoldABC import HoldABC

__all__ = [
    "HoldList",
]


@deco.dataDeco()
class HoldList(DataList, HoldABC):
    __slots__ = ()
    data: tuple
