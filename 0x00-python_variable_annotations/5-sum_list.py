#!/usr/bin/env python3
"""It contains a process that adds a list of floats"""

from typing import List


def sum_list(input_list: List[float]) -> float:
    """
    It adds the sum of a list of integers.
    """
    total = 0.0
    for number in input_list:
        total += number
    return total
