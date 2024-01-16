#!/usr/bin/env python3
""" Write a coroutine called async_generator
that takes no arguments."""

import asyncio
from typing import List, Generator
import time
import random


async def async_generator() -> Generator[float, None, None]:
    """ Write a coroutine called async_generator
    that takes no arguments."""
    i = 0
    while (i < 10):
        yield random.uniform(0, 10)
        i = i + 1
        await asyncio.sleep(1)
