from typing import *

from datahold.core.DataABC import DataABC

__all__ = ["HoldABC"]


class HoldABC(DataABC):
    __slots__ = ("_data",)
