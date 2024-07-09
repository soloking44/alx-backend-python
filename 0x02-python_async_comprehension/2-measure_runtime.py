#!/usr/bin/env python3
"""
Implement a coroutine measure_runtime to execute async_comprehension.
"""

import time
import asyncio

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    Execute async_comprehension() 4 times in dual
    in other to measure the total runtime.
    """
    start_time = time.time()

    await asyncio.gather(*(async_comprehension() for k in range(4)))
