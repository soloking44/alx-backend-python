#!/usr/bin/env python3
"""
It has a function that increases a float by multiplier.
"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    It generates a multiplier process.
    """
    return lambda x: x * multiplier
