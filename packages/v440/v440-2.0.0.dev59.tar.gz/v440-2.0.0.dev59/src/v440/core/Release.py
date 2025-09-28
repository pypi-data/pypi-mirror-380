from __future__ import annotations

import operator
import string
from typing import *

import setdoc
from keyalias import keyalias
from overloadable import Overloadable

from v440._utils import utils
from v440._utils.utils import guard
from v440._utils.VList import VList

__all__ = ["Release"]


@Overloadable
def tolist(value: Any, *, slicing: Any) -> list:
    if value is None:
        return
    if isinstance(value, int):
        return int
    if hasattr(value, "__iter__") and not isinstance(value, str):
        return list
    return str


@tolist.overload()
def tolist(value: None, *, slicing: Any) -> list:
    return list()


@tolist.overload(int)
def tolist(value: int, *, slicing: Any) -> list:
    v: int = int(value)
    if value < 0:
        raise ValueError
    return [v]


@tolist.overload(list)
def tolist(value: int, *, slicing: Any) -> list:
    return list(map(utils.numeral, value))


@tolist.overload(str)
def tolist(value: Any, *, slicing: Any) -> list:
    s: Any
    if isinstance(value, str):
        s = slicing
    else:
        s = "never"
    v: str = str(value)
    if v == "":
        return list()
    if "" == v.strip(string.digits) and s in (len(v), "always"):
        return list(map(int, v))
    v = v.lower().strip()
    v = v.replace("_", ".")
    v = v.replace("-", ".")
    if v.startswith("v") or v.startswith("."):
        v = v[1:]
    l: list = v.split(".")
    if "" in l:
        raise ValueError
    l = list(map(utils.numeral, l))
    return l


def torange(key: Any, length: Any) -> range:
    start: Any = key.start
    stop: Any = key.stop
    step: Any = key.step
    if step is None:
        step = 1
    else:
        step = operator.index(step)
        if step == 0:
            raise ValueError
    fwd: bool = step > 0
    if start is None:
        start = 0 if fwd else (length - 1)
    else:
        start = operator.index(start)
    if stop is None:
        stop = length if fwd else -1
    else:
        stop = operator.index(stop)
    if start < 0:
        start += length
    if start < 0:
        start = 0 if fwd else -1
    if stop < 0:
        stop += length
    if stop < 0:
        stop = 0 if fwd else -1
    ans: range = range(start, stop, step)
    return ans


@keyalias(major=0, minor=1, micro=2, patch=2)
class Release(VList):
    __slots__ = ()

    data: tuple[int]
    major: int
    minor: int
    micro: int
    patch: int

    @Overloadable
    @setdoc.basic
    def __delitem__(self: Self, key: Any) -> bool:
        return type(key) is slice

    @__delitem__.overload(False)
    @setdoc.basic
    def __delitem__(self: Self, key: SupportsIndex) -> None:
        i: int = operator.index(key)
        if i >= len(self):
            return
        data: list = list(self.data)
        del data[i]
        self.data = data

    @__delitem__.overload(True)
    @setdoc.basic
    def __delitem__(self: Self, key: Any) -> None:
        r: range = torange(key, len(self))
        k: Any
        l: list = [k for k in r if k < len(self)]
        l.sort(reverse=True)
        data: list = list(self.data)
        for k in l:
            del data[k]
        self.data = data

    @Overloadable
    @setdoc.basic
    def __getitem__(self: Self, key: Any) -> bool:
        return type(key) is slice

    @__getitem__.overload(False)
    @setdoc.basic
    def __getitem__(self: Self, key: Any) -> int:
        i: int = operator.index(key)
        ans: int = self._getitem_int(i)
        return ans

    @__getitem__.overload(True)
    @setdoc.basic
    def __getitem__(self: Self, key: Any) -> list:
        r: range = torange(key, len(self))
        m: map = map(self._getitem_int, r)
        ans: list = list(m)
        return ans

    @setdoc.basic
    def __init__(self: Any, data: Any = None) -> None:
        self.data = data

    @Overloadable
    @setdoc.basic
    def __setitem__(self: Self, key: Any, value: Any) -> bool:
        return type(key) is slice

    @__setitem__.overload(False)
    @setdoc.basic
    def __setitem__(self: Self, key: SupportsIndex, value: Any) -> Any:
        i: int = operator.index(key)
        self._setitem_int(i, value)

    @__setitem__.overload(True)
    @setdoc.basic
    def __setitem__(self: Self, key: SupportsIndex, value: Any) -> Any:
        k: range = torange(key, len(self))
        self._setitem_range(k, value)

    def _format(self: Self, format_spec: str) -> str:
        i: Optional[int]
        if format_spec:
            i = int(format_spec)
        else:
            i = None
        l: list = self[:i]
        if len(l) == 0:
            l += [0]
        l = list(map(str, l))
        ans: str = ".".join(l)
        return ans

    def _getitem_int(self: Self, key: int) -> int:
        if key < len(self):
            return self.data[key]
        else:
            return 0

    def _setitem_int(self: Self, key: int, value: Any) -> Any:
        v: int = utils.numeral(value)
        if key < len(self):
            data = list(self.data)
            data[key] = v
            self.data = data
            return
        if v == 0:
            return
        self._data += (0,) * (key - len(self))
        self._data += (v,)

    @Overloadable
    def _setitem_range(self: Self, key: range, value: Any) -> bool:
        return key.step == 1

    @_setitem_range.overload(False)
    def _setitem_range(self: Self, key: range, value: Any) -> Any:
        key: list = list(key)
        value: list = tolist(value, slicing=len(key))
        if len(key) != len(value):
            e = "attempt to assign sequence of size %s to extended slice of size %s"
            e %= (len(value), len(key))
            raise ValueError(e)
        ext: int = max(0, max(*key) + 1 - len(self))
        data: list = list(self.data)
        data += [0] * ext
        for k, v in zip(key, value):
            data[k] = v
        self.data = data

    @_setitem_range.overload(True)
    def _setitem_range(self: Self, key: range, value: Any) -> Any:
        data: list = list(self.data)
        ext: int = max(0, key.start - len(data))
        data += ext * [0]
        l: list = tolist(value, slicing="always")
        data = data[: key.start] + l + data[key.stop :]
        self.data = data

    @classmethod
    def _sort(cls: type, value: int) -> int:
        return value

    def bump(self: Self, index: SupportsIndex = -1, amount: SupportsIndex = 1) -> None:
        i: int = operator.index(index)
        a: int = operator.index(amount)
        x: int = self._getitem_int(i) + a
        self._setitem_int(i, x)
        if i != -1:
            self.data = self.data[: i + 1]

    @property
    @setdoc.basic
    def data(self: Self) -> tuple:
        return self._data

    @data.setter
    @guard
    def data(self: Self, value: Any) -> None:
        v: list = tolist(value, slicing="always")
        while v and v[-1] == 0:
            v.pop()
        self._data = tuple(v)
