#!/usr/bin/env python3
"""
It has a function’s and annotated parameters that return values
with a given type
"""
from typing import Iterable, List, Sequence, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    It adds the length of a list of sequences.
    """
    return [(i, len(i)) for i in lst]
