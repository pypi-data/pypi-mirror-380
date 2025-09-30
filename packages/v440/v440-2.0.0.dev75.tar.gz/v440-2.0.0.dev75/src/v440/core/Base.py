from __future__ import annotations

from typing import *

import setdoc
from overloadable import Overloadable

from v440._utils.Digest import Digest
from v440._utils.guarding import guard
from v440._utils.SlotStringer import SlotStringer
from v440.core.Release import Release

__all__ = ["Base"]


parse_epoch: Digest = Digest("parse_epoch")


@parse_epoch.overload()
def parse_epoch() -> int:
    return 0


@parse_epoch.overload(int)
def parse_epoch(value: int) -> int:
    if value < 0:
        raise ValueError
    return value


@parse_epoch.overload(str)
def parse_epoch(value: str) -> int:
    s: str = value
    if s.endswith("!"):
        s = s[:-1]
    if s == "":
        return 0
    ans: int = int(s)
    if ans < 0:
        raise ValueError
    return ans


class Base(SlotStringer):

    __slots__ = ("_epoch", "_release")

    string: str
    epoch: int
    release: Release

    def __bool__(self: Self) -> bool:
        return bool(self.epoch or self.release)

    @Overloadable
    @setdoc.basic
    def __init__(self: Self, *args: Any, **kwargs: Any) -> bool:
        if len(args) == 0 and "string" in kwargs.keys():
            return True
        if len(args) == 1 and len(kwargs) == 0:
            return True
        return False

    @__init__.overload(True)
    @setdoc.basic
    def __init__(self: Self, string: Any) -> None:
        self._init_setup()
        self.string = string

    @__init__.overload(False)
    @setdoc.basic
    def __init__(
        self: Self,
        epoch: Any = "0",
        release: Any = "0",
    ) -> None:
        self._init_setup()
        self.epoch = epoch
        self.release = release

    def _init_setup(self: Self) -> None:
        self._epoch = 0
        self._release = Release()

    def _format(self: Self, format_spec: str) -> str:
        ans: str = ""
        if self.epoch:
            ans += "%s!" % self.epoch
        ans += format(self.release, format_spec)
        return ans

    def _string_fset(self: Self, value: str) -> None:
        v: str = value
        if v.startswith("v"):
            v = v[1:]
        parsed: Iterable
        if "!" in v:
            parsed = v.split("!")
        else:
            parsed = 0, v
        self.epoch, self.release.string = parsed

    def _todict(self: Self) -> dict:
        return dict(epoch=self.epoch, release=self.release)

    @property
    def epoch(self: Self) -> int:
        "This property represents the epoch."
        return self._epoch

    @epoch.setter
    @guard
    def epoch(self: Self, value: Any) -> None:
        self._epoch = parse_epoch(value)

    @property
    def release(self: Self) -> Release:
        "This property represents the release."
        return self._release

    @release.setter
    @guard
    def release(self: Self, value: Any) -> None:
        self.release._set(value)
