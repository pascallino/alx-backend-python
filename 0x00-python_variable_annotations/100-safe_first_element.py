#!/usr/bin/env python3
'''Task 9's module.
'''
from typing import Iterable, List, Sequence, Tuple, Union, Any


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """ test file"""
    if lst:
        return lst[0]
    else:
        return None
