# -*- coding: utf-8 -*-

"""
Test utilities for requests HTTP client library.

This module provides specialized test case utilities for testing code that uses
the popular requests library. It extends the base HTTP test functionality with
requests-specific mock objects and response simulation.

Key features:
- Mock requests.Response objects with realistic behavior
- Support for JSON, text, and binary content responses
- Status code validation and error simulation
- Streaming response support with iter_content and iter_lines
- Automatic content encoding and type handling

Example:
    Basic requests response mocking::

        from core_https.tests.requests_ import BaseRequestsTestCases

        class MyRequestsTest(BaseRequestsTestCases):
            def test_json_response(self):
                mock_response = self.get_requests_mock(
                    json_response={"users": ["alice", "bob"]},
                    status_code=200
                )

                # Test synchronous methods
                self.assertEqual(mock_response.status_code, 200)
                self.assertEqual(mock_response.json()["users"], ["alice", "bob"])
                self.assertTrue(mock_response.ok)

See Also:
    - BaseHttpTestCases: Base class for HTTP testing utilities
    - BaseAiohttpTestCases: Test utilities for aiohttp library
    - BaseUrllib3TestCases: Test utilities for urllib3 library
"""

import json
from typing import Any, Dict, Optional
from unittest.mock import Mock

from core_https.tests.base import BaseHttpTestCases


class BaseRequestsTestCases(BaseHttpTestCases):
    """
    Test utilities for requests HTTP client library.

    This class provides specialized methods for creating mock requests.Response
    objects that behave like real HTTP responses. It extends BaseHttpTestCases
    with requests-specific functionality including JSON handling, content encoding,
    and status code validation.

    The class is designed to simplify testing of code that uses the requests
    library by providing pre-configured mock objects that match requests'
    response interface and behavior.

    Example:
        Creating mock responses for different scenarios::

            class MyRequestsTest(BaseRequestsTestCases):
                def test_successful_api_call(self):
                    mock = self.get_requests_mock(
                        json_response={"id": 123, "name": "Alice"},
                        status_code=201
                    )

                    self.assertEqual(mock.status_code, 201)
                    self.assertTrue(mock.ok)
                    self.assertEqual(mock.json()["name"], "Alice")

                def test_error_handling(self):
                    mock = self.get_requests_mock(
                        status_code=404,
                        raise_for_status_exception=requests.HTTPError("Not Found")
                    )

                    self.assertFalse(mock.ok)
                    with self.assertRaises(requests.HTTPError):
                        mock.raise_for_status()

        Testing streaming responses::

            def test_streaming_content(self):
                content = b"line1\\nline2\\nline3"
                mock = self.get_requests_mock(content=content)

                # Test streaming methods
                for chunk in mock.iter_content():
                    self.assertIsInstance(chunk, bytes)

                lines = list(mock.iter_lines())
                self.assertEqual(len(lines), 3)

    Note:
        The mock objects created by this class include all standard requests.Response
        attributes and methods, making them suitable for comprehensive testing of
        requests-based code.
    """

    @classmethod
    def get_requests_mock(
        cls,
        url: str = "https://example.com",
        encoding: str = "utf-8",
        headers: Optional[Dict[str, str]] = None,
        json_response: Optional[Dict[str, Any]] = None,
        text_response: Optional[str] = None,
        status_code: int = 200,
        content: Optional[bytes] = None,
        raise_for_status_exception: Optional[Exception] = None,
    ) -> Mock:
        """
        Create a mock requests.Response object for testing.

        This method creates a comprehensive mock of requests.Response with all
        standard attributes and methods. It automatically handles content type
        conversions and provides realistic response behavior for testing.

        Args:
            url: The URL that the mock response represents. Defaults to "https://example.com".
            encoding: Character encoding for text content. Defaults to "utf-8".
            headers: Dictionary of response headers. Auto-generated if not provided.
            json_response: JSON data to return from the .json() method. Mutually exclusive with text_response.
            text_response: Plain text content. Auto-generated from json_response if not provided.
            status_code: HTTP status code for the response. Defaults to 200.
            content: Raw bytes content. Auto-generated from text_response if not provided.
            raise_for_status_exception: Exception to raise when .raise_for_status() is called.

        Returns:
            Mock object simulating requests.Response with all standard methods and attributes.

        Example:
            Creating a JSON response mock::

                mock_response = BaseRequestsTestCases.get_requests_mock(
                    json_response={"id": 123, "name": "Alice"},
                    status_code=201,
                    headers={"Location": "/users/123"}
                )

                # Test standard response properties
                self.assertEqual(mock_response.status_code, 201)
                self.assertTrue(mock_response.ok)
                self.assertEqual(mock_response.json()["name"], "Alice")

            Creating an error response::

                import requests
                error_mock = BaseRequestsTestCases.get_requests_mock(
                    status_code=404,
                    text_response="Not Found",
                    raise_for_status_exception=requests.HTTPError("404 Not Found")
                )

                # Test error handling
                self.assertFalse(error_mock.ok)
                with self.assertRaises(requests.HTTPError):
                    error_mock.raise_for_status()

            Testing streaming content::

                stream_mock = BaseRequestsTestCases.get_requests_mock(
                    content=b"chunk1\\nchunk2\\nchunk3"
                )

                # Test streaming methods
                chunks = list(stream_mock.iter_content())
                lines = list(stream_mock.iter_lines())
                self.assertEqual(len(lines), 3)

        Note:
            - If json_response is provided, text_response is auto-generated as JSON string
            - If text_response is provided, content is auto-generated as encoded bytes
            - The mock includes iter_content and iter_lines for streaming support
            - Status codes < 400 automatically set the 'ok' property to True
        """

        if json_response is None:
            json_response = {}

        if headers is None:
            headers = {
                "Content-Type": "application/json",
            }

        if text_response is None:
            text_response = json.dumps(json_response) if json_response else ""

        if content is None:
            content = text_response.encode(encoding)

        mock = Mock()

        mock.status_code = status_code
        mock.headers = headers
        mock.url = url
        mock.encoding = encoding
        mock.text = text_response
        mock.content = content

        mock.ok = status_code < 400
        mock.reason = cls.code_mapper.get(status_code)
        mock.json.return_value = json_response

        mock.raise_for_status.return_value = None
        if raise_for_status_exception:
            mock.raise_for_status.side_effect = raise_for_status_exception

        # Support for iter_content and iter_lines (common in streaming)...
        mock.iter_content.return_value = iter([content])
        mock.iter_lines.return_value = iter(text_response.splitlines())
        return mock
