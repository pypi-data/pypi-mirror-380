# -*- coding: utf-8 -*-

"""
Base test case classes for HTTP request testing.

This module provides the foundational base class for HTTP-related testing in the
core_https library. It serves as the parent class for specialized test utilities
that mock different HTTP libraries (requests, aiohttp, urllib3).

The base class provides common functionality and utilities that are shared across
all HTTP library testing implementations.

Example:
    Creating a custom HTTP test class::

        from core_https.tests.base import BaseHttpTestCases

        class MyHttpTests(BaseHttpTestCases):
            def test_status_code_mapping(self):
                # Access HTTP status code mappings
                self.assertEqual(self.code_mapper[200], "OK")
                self.assertEqual(self.code_mapper[404], "Not Found")

See Also:
    - BaseRequestsTestCases: Specialized test utilities for requests library
    - BaseAiohttpTestCases: Specialized test utilities for aiohttp library
    - BaseUrllib3TestCases: Specialized test utilities for urllib3 library
"""

from typing import Dict
from unittest import TestCase

from core_https.utils import HTTPStatus


class BaseHttpTestCases(TestCase):
    """
    Base class for HTTP request test cases.

    This class serves as the foundation for all HTTP library testing utilities
    in the core_https package. It extends unittest.TestCase and provides common
    functionality shared across different HTTP client testing implementations.

    The class primarily provides access to HTTP status code mappings through
    the code_mapper attribute, which can be used in test assertions and
    mock response creation.

    Attributes:
        code_mapper: Dictionary mapping HTTP status codes (int) to their
            corresponding reason phrases (str). Generated from HTTPStatus enum.

    Example:
        Basic usage in test methods::

            class MyHttpTest(BaseHttpTestCases):
                def test_successful_response(self):
                    # Use the inherited code_mapper
                    self.assertEqual(self.code_mapper[200], "OK")
                    self.assertEqual(self.code_mapper[201], "Created")

                def test_error_responses(self):
                    # Access various error status descriptions
                    self.assertEqual(self.code_mapper[400], "Bad Request")
                    self.assertEqual(self.code_mapper[404], "Not Found")
                    self.assertEqual(self.code_mapper[500], "Internal Server Error")

        Using with mock responses::

            def create_mock_response(self, status_code: int):
                return {
                    "status_code": status_code,
                    "reason": self.code_mapper.get(status_code, "Unknown Status"),
                    "content": b'{"message": "test response"}'
                }

    Note:
        This class is designed to be extended by specialized test utilities for
        specific HTTP libraries. Direct instantiation is possible but typically
        not necessary as subclasses provide more specific functionality.

    See Also:
        - BaseRequestsTestCases: For testing code that uses the requests library
        - BaseAiohttpTestCases: For testing code that uses the aiohttp library
        - BaseUrllib3TestCases: For testing code that uses the urllib3 library
        - HTTPStatus: The enum class providing status code definitions
    """

    code_mapper: Dict[int, str] = HTTPStatus.as_dict()
