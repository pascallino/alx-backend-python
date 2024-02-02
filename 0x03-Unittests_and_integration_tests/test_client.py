#!/usr/bin/env python3
""" testing  unit test for client"""
import unittest
from unittest.mock import patch
from parameterized import parameterized
from client import GithubOrgClient  # Assuming client module is available
from unittest.mock import (
    MagicMock,
    Mock,
    PropertyMock,
    patch,
)
from typing import Dict
from parameterized import parameterized, parameterized_class
from requests import HTTPError


class TestGithubOrgClient(unittest.TestCase):
    """ test class gituporg"""
    @parameterized.expand([
        ("google", {'login': "google"}),
        ("abc", {'login': "abc"}),
    ])
    @patch('client.get_json')
    def test_org(self, org_name, resp: Dict, get_json_mock: MagicMock):
        """ function to test gituporg"""
        # Create an instance of GithubOrgClient with the org_name
        github_client = GithubOrgClient(org_name)
        get_json_mock.return_value = MagicMock(return_value=resp)
        # Assert that get_json was called once with the expected URL
        self.assertEqual(github_client.org(), resp)
        github_client_url = GithubOrgClient.ORG_URL.format(org=org_name)
        get_json_mock.assert_called_once_with(
            "https://api.github.com/orgs/{}".format(org_name)
        )
