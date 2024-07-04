#!/usr/bin/env python3
"""
It has a process that adds the sum_mixed_list
"""

from typing import List, Union


def sum_mixed_list(mixed_list: List[Union[int, float]]) -> float:
    """
    It adds the sum of a list of integers and values.
    """
    total = 0.0
    for num in mixed_list:
        total += num
    return total
