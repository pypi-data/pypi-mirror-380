import abc
from functools import partial
from typing import *

import setdoc

__all__ = ["dataDeco"]


def dataDeco() -> partial:
    return update


def update(
    Target: type,
) -> type:
    Target.data = makeData(Target)
    abc.update_abstractmethods(Target)
    return Target


def makeData(Target: type) -> property:
    Frozen: type = Target.__annotations__["data"]

    def fget(self: Self) -> Any:
        return self._data

    adapt(fget, Target=Target)

    def fset(self: Self, value: Any) -> None:
        self._data = Frozen(value)

    adapt(fset, Target=Target)

    ans: property = property(
        fget=fget,
        fset=fset,
        doc=setdoc.getbasicdoc("data"),
    )
    return ans


def adapt(func: Callable, *, Target: type) -> None:
    func.__module__ = Target.__module__
    func.__qualname__ = Target.__qualname__ + ".data." + func.__name__
    func.__name__ = "data"
