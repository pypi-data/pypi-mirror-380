import collections
from abc import abstractmethod
from typing import *

import setdoc
from datarepr import datarepr
from overloadable import Overloadable

from v440._utils.BaseList import BaseList
from v440._utils.utils import guard

__all__ = ["VList"]


class VList(BaseList, collections.abc.MutableSequence):

    __slots__ = ("_data",)
    data: tuple
    string: str

    @setdoc.basic
    def __add__(self: Self, other: Any) -> Self:
        return type(self)(self.data + tuple(other))

    @setdoc.basic
    def __bool__(self: Self) -> bool:
        return bool(self.data)

    @setdoc.basic
    def __delitem__(self: Self, key: Any) -> None:
        data: list = list(self.data)
        del data[key]
        self.data = data

    @setdoc.basic
    def __iadd__(self: Self, other: Any, /) -> Self:
        self.data = self.data + tuple(other)
        return self

    @setdoc.basic
    def __imul__(self: Self, other: Any, /) -> Self:
        self.data = self.data * other
        return self

    @setdoc.basic
    def __len__(self: Self) -> int:
        return len(self.data)

    @setdoc.basic
    def __mul__(self: Self, other: Any) -> Self:
        return type(self)(self.data * other)

    @setdoc.basic
    def __rmul__(self: Self, other: Any) -> Self:
        return self * other

    def _cmp(self: Self) -> tuple:
        return tuple(map(self._sort, self.data))

    @classmethod
    @abstractmethod
    def _sort(cls: type, value: Any): ...

    def _todict(self: Self) -> dict:
        return dict(data=self.data)

    def append(self: Self, value: Self, /) -> None:
        "This method appends value to self."
        data: list = list(self.data)
        data.append(value)
        self.data = data

    def clear(self: Self) -> None:
        "This method clears the data."
        self.data = ()

    def extend(self: Self, value: Self, /) -> None:
        "This method extends self by value."
        data: list = list(self.data)
        data.extend(value)
        self.data = data

    def insert(
        self: Self,
        index: SupportsIndex,
        value: Any,
        /,
    ) -> None:
        "This method inserts value at index."
        data: list = list(self.data)
        data.insert(index, value)
        self.data = data

    def pop(self: Self, index: SupportsIndex = -1, /) -> Any:
        "This method pops an item."
        data: list = list(self.data)
        ans: Any = data.pop(index)
        self.data = data
        return ans

    def remove(self: Self, value: Any, /) -> None:
        "This method removes the first occurence of value."
        data: list = list(self.data)
        data.remove(value)
        self.data = data

    def reverse(self: Self) -> None:
        "This method reverses the order of the data."
        data: list = list(self.data)
        data.reverse()
        self.data = data

    def sort(self: Self, *, key: Any = None, reverse: Any = False) -> None:
        "This method sorts the data."
        data: list = list(self.data)
        k: Any = self._sort if key is None else key
        r: bool = bool(reverse)
        data.sort(key=k, reverse=r)
        self.data = data

    # data-associated
    @setdoc.basic
    def __contains__(self: Self, other: Any) -> bool:
        return other in self.data

    @setdoc.basic
    def __getitem__(self: Self, key: Any) -> Any:
        return self.data[key]

    @Overloadable
    @setdoc.basic
    def __init__(self: Self, *args: Any, **kwargs: Any) -> bool:
        if len(args) == 0 and "string" in kwargs.keys():
            return True
        if len(args) == 1 and len(kwargs) == 0:
            if isinstance(args[0], str):
                return True
            if hasattr(args[0], "__iter__"):
                return False
            return True
        return False

    @__init__.overload(True)
    @setdoc.basic
    def __init__(self: Self, string: Any) -> None:
        self._init_setup()
        self.string = string

    @__init__.overload(False)
    @setdoc.basic
    def __init__(self: Self, data: Iterable = ()) -> None:
        self._init_setup()
        self.data = data

    @setdoc.basic
    def __iter__(self: Self) -> Iterator:
        return iter(self.data)

    @setdoc.basic
    def __repr__(self: Self) -> str:
        return datarepr(type(self).__name__, *self.data)

    @setdoc.basic
    def __reversed__(self: Self) -> reversed:
        return reversed(self.data)

    @setdoc.basic
    def __setitem__(self: Self, key: Any, value: Any) -> None:
        data: list = list(self.data)
        data[key] = value
        self.data = data

    @classmethod
    @abstractmethod
    def _data_parse(cls: type, value: list) -> Iterable: ...

    def _init_setup(self: Self) -> None:
        self._data = ()

    def _set(self: Self, value: Any) -> None:
        if value is None:
            self.data = ()
        elif isinstance(value, str):
            self.string = value
        elif hasattr(value, "__iter__"):
            self.data = value
        else:
            self.string = value

    @property
    @setdoc.basic
    def data(self: Self) -> tuple:
        return self._data

    @data.setter
    @guard
    def data(self: Self, value: Iterable) -> None:
        self._data = tuple(self._data_parse(list(value)))

    def count(self: Self, value: Any) -> int:
        "This method counts the occurences of value."
        return self.data.count(value)

    def index(self: Self, *args: Any) -> None:
        "This method returns the index of the first occurence."
        return self.data.index(*args)
