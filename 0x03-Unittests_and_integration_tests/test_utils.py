#!/usr/bin/env python3
""" testing parameterized unit test for nested map"""
import unittest
from parameterized import parameterized
from unittest.mock import patch, Mock
from utils import get_json, memoize
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


class TestGetJson(unittest.TestCase):
    """Tests the `get_json` function."""
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
            # Call the get_json function
            result = get_json(test_url)

            # Assert that requests.get was called exactly
            # once with the test_url
            mock_get.assert_called_once_with(test_url)


class TestMemoize(unittest.TestCase):
    """ class to test for memorization"""

    def test_memoize(self):
        """ test momorization """
        class TestClass:
            """ test class for a attr """
            def a_method(self):
                """" test s_methos"""
                return 42

            @memoize
            def a_property(self):
                """" test a property"""
                return self.a_method()

        # Mock the a_method using patch
        with patch.object(TestClass, "a_method",
                          return_value=lambda: 42) as mock_a_method:
            test_instance = TestClass()
            # Call a_property twice
            result1 = test_instance.a_property()
            result2 = test_instance.a_property()
            # Assert that the results are correct
            self.assertEqual(result1, 42)
            self.assertEqual(result2, 42)
            # Assert that a_method was called only once
            mock_a_method.assert_called_once()
