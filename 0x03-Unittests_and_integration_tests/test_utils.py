#!/usr/bin/env python3
""" testing parameterized unit test for nested map"""
import unittest
from parameterized import parameterized
from unittest.mock import patch, Mock
from utils import get_json
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

    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False}),
    ])
    def test_get_json(self, test_url, test_payload):
        """Tests the `get_json` function."""
        # Create a Mock object with a json method that returns the test_payload
        # Patch requests.get to return the mock_response
        attrs = {'json.return_value': test_payload}
        with patch('requests.get',
                   return_value=Mock(**attrs)) as mock_get:
            # Assert that the result of get_json is equal to the test_payload
            self.assertEqual(get_json(test_url), test_payload)
            # Assert that requests.get was called exactly
            # once with the test_url
            mock_get.assert_called_once_with(test_url)
