import enum
import functools
import tomllib
from importlib import resources
from typing import *

__all__ = ["Cfg"]


class Cfg(enum.Enum):
    "This enum provides a singleton."
    cfg = None

    @functools.cached_property
    def data(self: Self) -> dict:
        "This cached property holds the cfg data."
        text: str = resources.read_text("datahold._utils", "cfg.toml")
        ans: dict = tomllib.loads(text)
        return ans
