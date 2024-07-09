#!/usr/bin/env python3
"""
Implement a coroutine named async_comprehension that does not accept arguments.
"""

import asyncio
from typing import List

async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    '''Creates a set of 10 numbers in 10-number generator.
    '''
    return [x async for x in async_generator()]
