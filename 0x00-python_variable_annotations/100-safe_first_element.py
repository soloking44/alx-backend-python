#!/usr/bin/env python3
"""
It has the code with the right duck-typed annotations
"""

from typing import Any, Sequence, Union


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """
    It fetches the first element of a sequence.
    """
    if lst:
        return lst[0]
    else:
        return None
