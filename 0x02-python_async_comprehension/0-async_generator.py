#!/usr/bin/env python3
"""
This implement a coroutine named async_generator that does not accept any arguments.
"""

import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """
    This creates a sequence of 10 numbers asynchronously.
    """
    for k in range(10):
        await asyncio.sleep(1)
        yield random.random() * 10
