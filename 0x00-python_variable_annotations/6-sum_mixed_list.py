#!/usr/bin/env python3
""" Write a type-annotated function sum_mixed_list
which takes a list mxd_lst of integers and
floats and returns their sum as a float
"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """ sum_mixed_list function annotations """
    return sum(mxd_lst)
