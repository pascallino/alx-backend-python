#!/usr/bin/env python3

import asyncio

task_wait_random = __import__('3-tasks').task_wait_random


async def test(max_delay: int) -> float:
    task = task_wait_random(max_delay)
    val = await task
    print(task.__class__)
    print(val)

asyncio.run(test(5))