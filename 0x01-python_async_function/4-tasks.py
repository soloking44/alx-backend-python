#!/usr/bin/env python3
"""
This writes a process do not create an async function.
"""

import asyncio
from typing import List

task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    '''This initiates task_wait_random n times.
    '''
    wait_times = await asyncio.gather(
        *tuple(task_wait_random(max_delay) for i in range(n))
    )
    return sorted(wait_times)
