#!/usr/bin/env python3
""" Take the code from wait_n and
alter it into a new function task_wait_n. The code is nearly
identical to wait_n except
task_wait_random is being called."""
import asyncio
from typing import List
import time

wait_n = __import__('1-concurrent_coroutines').wait_n
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """ task  pythonasync project"""
    task = task_wait_random(max_delay)
    task = [task_wait_random(max_delay) for i in range(n)]
    all_list = await asyncio.gather(*task)
    return sorted(all_list)
