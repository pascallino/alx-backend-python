#!/usr/bin/env python3
""" testing parameterized unit test for nested map"""
import unittest
from parameterized import parameterized
from utils import access_nested_map  # Assuming utils module is available


class TestAccessNestedMap(unittest.TestCase):
    """ class to test Access maps"""

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
    ])
    def test_access_nested_map(self, nested_map, path, expected_result):
        """ function to test the acces mapd"""
        self.assertEqual(access_nested_map(nested_map, path), expected_result)

    @parameterized.expand([
        ({}, ("a",), KeyError),
        ({"a": 1}, ("a", "b"), KeyError),
    ])
    def test_access_nested_map_exception(self, nested_map, path,
                                         exception: Exception,):
        """ test with assert raises error to see if the error message match """
        with self.assertRaises(KeyError) as context:
            access_nested_map(nested_map, path)
