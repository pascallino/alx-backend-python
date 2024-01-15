#!/usr/bin/env python3
""" Write an asynchronous coroutine that takes
in an integer argument (max_delay, with a default
value of 10) named wait_random that waits
for a random delay between 0 and max_delay
(included and float value) seconds and eventually returns it.
Use the random module. """
import random
import asyncio


async def wait_random(max_delay: int = 10):
    """ task 0 for async project"""
    await asyncio.sleep(random.uniform(0, max_delay))
    return random.uniform(0, max_delay)
