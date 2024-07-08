#!/usr/bin/env python3
"""
This writes async routine that is called wait_n to take 2 integer arguments
"""

import asyncio
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    '''It executes wait_random n times.

    Args:
        n (int): Number of times to spawn wait_random.
        max_delay (int): Maximum number of seconds to wait for.

    Returns:
        List[float]: List of all the delays in ascending order.
    '''
    # create a list to store all the tasks
    tasks = [asyncio.create_task(wait_random(max_delay)) for i in range(n)]

    # wait for all tasks to complete and gather their results
    delays = await asyncio.gather(*tasks)

    # return the list of delays sorted in ascending order
    return sorted(delays)
