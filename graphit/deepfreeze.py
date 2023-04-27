from functools import singledispatch
from typing import Optional, Union
#
from frozendict import frozendict


@singledispatch
def deepfreeze(data):
    """
    Recursively freezes all data. Main use case is data serialized from json/yaml/toml.
    Converts dictionaries to frozendict and some list-like containers to tuple.
    Handles built-in primitive immutable values, such as numbers and strings.
    Type support can be extended using the singledispatch syntax.
    """
    raise NotImplementedError(f"Class {type(data)} has no deepfreeze implementation.")


@deepfreeze.register
def _(data: Optional[Union[int, float, str, bytes]]):
    # already immutable, return as is
    return data


@deepfreeze.register
def _(data: dict):
    # dict to frozendict, recursive deepfreeze on all values
    return frozendict({k: deepfreeze(v) for k, v in data.items()})


# all list-like containers shall become tuples


@deepfreeze.register
def _(data: list):
    return tuple(deepfreeze(e) for e in data)


@deepfreeze.register
def _(data: tuple):
    return tuple(deepfreeze(e) for e in data)


@deepfreeze.register
def _(data: set):
    return tuple(deepfreeze(e) for e in data)


@deepfreeze.register
def _(data: frozenset):
    return tuple(deepfreeze(e) for e in data)
