#!/usr/bin/env python3
"""
This asynchronous basics that takes an integer argument
"""

import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """
    It waits for a random number of seconds.
    """
    wait_time = random.uniform(0, max_delay)
    await asyncio.sleep(wait_time)
    return wait_time
