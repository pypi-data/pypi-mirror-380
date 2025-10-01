# -*- coding: utf-8 -*-

"""
Test utilities for aiohttp HTTP client library.

This module provides specialized test case utilities for testing code that uses
the aiohttp library. It extends the base HTTP test functionality with aiohttp-specific
mock objects and utilities.

Key features:
- Mock ClientResponse objects with async method support
- Error simulation with ClientResponseError creation
- Case-insensitive header handling using CIMultiDict
- Async context manager support for response objects

Example:
    Basic aiohttp response mocking::

        from core_https.tests.aiohttp_ import BaseAiohttpTestCases

        class MyAiohttpTest(BaseAiohttpTestCases):
            def test_async_response(self):
                mock_response = self.get_aiohttp_mock(
                    json_response={"id": 123},
                    status=200
                )

                # Test async methods
                async def test():
                    json_data = await mock_response.json()
                    assert json_data["id"] == 123

                asyncio.run(test())

See Also:
    - BaseHttpTestCases: Base class for HTTP testing utilities
    - BaseRequestsTestCases: Test utilities for requests library
    - BaseUrllib3TestCases: Test utilities for urllib3 library
"""

from typing import Any, Dict, List, Optional
from unittest.mock import AsyncMock, Mock

from aiohttp import ClientResponseError
from multidict import CIMultiDict
from yarl import URL

from core_https.tests.base import BaseHttpTestCases
from core_https.tests.requests_ import BaseRequestsTestCases


class BaseAiohttpTestCases(BaseHttpTestCases):
    """
    Test utilities for aiohttp HTTP client library.

    This class provides specialized methods for creating mock aiohttp.ClientResponse
    objects and error instances. It extends BaseHttpTestCases with aiohttp-specific
    functionality including async method mocking and case-insensitive headers.

    The class is designed to simplify testing of code that uses aiohttp for HTTP
    requests by providing pre-configured mock objects that behave like real
    aiohttp responses.

    Example:
        Creating mock responses for testing::

            class MyAiohttpTest(BaseAiohttpTestCases):
                def test_json_response(self):
                    mock = self.get_aiohttp_mock(
                        json_response={"users": []},
                        status=200
                    )

                    async def test():
                        data = await mock.json()
                        assert data == {"users": []}

                    asyncio.run(test())

        Testing error conditions::

            def test_error_handling(self):
                error = self.create_client_response_error(
                    status=404,
                    message="Resource not found"
                )

                mock = self.get_aiohttp_mock(
                    status=404,
                    raise_for_status_exception=error
                )

                # Test error handling in your code
                pass

    Note:
        This class reuses some functionality from BaseRequestsTestCases for
        efficiency, adapting the mock objects for aiohttp-specific behavior.
    """

    @classmethod
    def get_aiohttp_mock(
        cls,
        url: str = "https://example.com",
        method: str = "GET",
        json_response: Optional[Dict[str, Any]] = None,
        status: int = 200,
        headers: Optional[Dict[str, str]] = None,
        text_response: Optional[str] = None,
        content: Optional[bytes] = None,
        content_type: str = "application/json",
        charset: str = "utf-8",
        raise_for_status_exception: Optional[Exception] = None,
    ) -> Mock:
        """
        Create a mock aiohttp.ClientResponse object for testing.

        This method creates a comprehensive mock of aiohttp's ClientResponse that
        supports async operations, case-insensitive headers, and context manager usage.
        The mock is based on a requests mock but adapted for aiohttp-specific behavior.

        Args:
            url: The URL that the mock response represents. Defaults to "https://example.com".
            method: HTTP method for the request. Defaults to "GET".
            json_response: JSON data to return from the async json() method.
            status: HTTP status code for the response. Defaults to 200.
            headers: Dictionary of response headers (case-insensitive).
            text_response: Plain text content to return from the async text() method.
            content: Raw bytes to return from the async read() method.
            content_type: MIME type for the Content-Type header. Defaults to "application/json".
            charset: Character encoding for the response. Defaults to "utf-8".
            raise_for_status_exception: Exception to raise when raise_for_status() is called.

        Returns:
            Mock object simulating aiohttp.ClientResponse with async method support.

        Example:
            Basic JSON response mock::

                mock_response = BaseAiohttpTestCases.get_aiohttp_mock(
                    json_response={"users": ["alice", "bob"]},
                    status=200
                )

                async def test():
                    async with mock_response as resp:
                        data = await resp.json()
                        assert len(data["users"]) == 2

            Error response simulation::

                error = ClientResponseError(...)
                mock_response = BaseAiohttpTestCases.get_aiohttp_mock(
                    status=500,
                    raise_for_status_exception=error
                )

        Note:
            The mock supports aiohttp-specific features like:
            - Async context manager protocol (__aenter__, __aexit__)
            - Case-insensitive headers using CIMultiDict
            - Async methods (json(), text(), read())
            - Standard aiohttp response attributes (status, method, url, etc.)
        """

        mock = BaseRequestsTestCases.get_requests_mock()
        del mock.status_code

        mock.status = status
        mock.method = method
        mock.url = url
        mock.charset = charset
        mock.content_type = content_type

        if headers is None:
            headers = {
                "Content-Type": f"{content_type}; charset={charset}",
            }

        # Headers as CIMultiDict (case-insensitive)...
        mock.headers = CIMultiDict(headers)

        # Async methods - these need to be AsyncMock to allow `await`...
        mock.json = AsyncMock(return_value=json_response)
        mock.text = AsyncMock(return_value=text_response)
        mock.read = AsyncMock(return_value=content)

        # Context manager support...
        mock.__aenter__ = AsyncMock(return_value=mock)
        mock.__aexit__ = AsyncMock(return_value=None)

        mock.raise_for_status.return_value = None
        if raise_for_status_exception:
            mock.raise_for_status.side_effect = raise_for_status_exception

        # History and other attributes...
        mock.history = []
        mock.cookies = {}
        return mock

    @staticmethod
    def create_client_response_error(
        url: str = "http://example.com",
        status: int = 404,
        message: str = "Not Found",
        history: Optional[List] = None,
    ) -> ClientResponseError:
        """
        Create a ClientResponseError for testing error handling.

        This utility method simplifies the creation of aiohttp.ClientResponseError
        instances for testing error conditions. It creates the necessary request_info
        mock and formats the error with proper history tracking.

        Args:
            url: The URL where the error occurred. Defaults to "http://example.com".
            status: HTTP status code for the error. Defaults to 404.
            message: Error message/reason phrase. Defaults to "Not Found".
            history: List of previous responses in redirect chain.

        Returns:
            ClientResponseError instance ready for use in tests.

        Example:
            Testing 404 error handling::

                error = BaseAiohttpTestCases.create_client_response_error(
                    url="https://api.example.com/users/999",
                    status=404,
                    message="User not found"
                )

                mock_response = self.get_aiohttp_mock(
                    status=404,
                    raise_for_status_exception=error
                )

                # Test your error handling code
                with self.assertRaises(ClientResponseError):
                    mock_response.raise_for_status()

            Testing server errors::

                server_error = BaseAiohttpTestCases.create_client_response_error(
                    status=500,
                    message="Internal Server Error"
                )

        Note:
            The created error includes a mock request_info object with the specified
            URL and basic request properties. The history parameter can be used to
            simulate redirect chains that led to the error.
        """

        request_info = Mock()
        request_info.url = URL(url)
        request_info.method = "GET"
        request_info.headers = {}

        if history is None:
            history = []

        return ClientResponseError(
            request_info=request_info,
            history=tuple(history),
            status=status,
            message=message,
        )
