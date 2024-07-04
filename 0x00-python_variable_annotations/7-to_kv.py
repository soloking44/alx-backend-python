#!/usr/bin/env python3
"""
It has a function that changes a Python var to kv.
"""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    It changes a Python var to a kv and squares it value.
    """
    return (k, float(v**2))
