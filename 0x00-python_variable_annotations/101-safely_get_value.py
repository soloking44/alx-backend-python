#!/usr/bin/env python3
"""
It has process that fetches value within a dictionary,
add type annotations to the process.
"""

from typing import Any, Mapping, Optional, TypeVar, Union

T = TypeVar('T')
Resp = Union[Any, T]
Defl = Union[T, None]


def safely_get_value(dct: Mapping, key: Any, default: Defl = None) -> Resp:
    """
    Fetches a value from a dictionary with a given key.
    """
    if key in dct:
        return dct[key]
    else:
        return default
