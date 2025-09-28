import abc
from functools import partial
from types import FunctionType
from typing import *

from datahold._utils.deco.wrapping import wrap

__all__ = ["initDeco"]


def initDeco(**kwargs: type) -> partial:
    return partial(update, **kwargs)


def update(
    Target: type,
    *,
    Frozen: type,
    NonFrozen: type,
) -> type:
    setupInit(
        Target=Target,
        Frozen=Frozen,
        NonFrozen=NonFrozen,
    )
    Target.__annotations__ = dict(data=Frozen)
    abc.update_abstractmethods(Target)
    return Target


def setupInit(*, Target: type, **kwargs: type) -> None:
    new: FunctionType = makeInit(**kwargs)
    new.__module__ = Target.__module__
    new.__name__ = "__init__"
    new.__qualname__ = Target.__qualname__ + ".__init__"
    Target.__init__ = new


def makeInit(*, Frozen: type, NonFrozen: type) -> FunctionType:
    def new(self: Self, *args: Any, **kwargs: Any) -> None:
        self.data = Frozen(*args, **kwargs)

    wrap(new=new, old=NonFrozen.__init__)

    return new
