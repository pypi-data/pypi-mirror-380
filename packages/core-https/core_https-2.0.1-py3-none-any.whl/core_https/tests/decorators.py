# -*- coding: utf-8 -*-

"""
Test decorators for HTTP library mocking.

This module provides decorators to mock HTTP requests for popular Python HTTP libraries:
  - aiohttp (async HTTP client).
  - requests (synchronous HTTP library).
  - urllib3 (low-level HTTP client).

These decorators simplify test setup by automatically patching the appropriate HTTP methods
and returning configurable mock responses.

Example:
    Basic usage with requests::

        @patch_requests(json_response={"id": 123}, status_code=201)
        def test_api_call(self):
            response = requests.get("https://api.example.com")
            assert response.status_code == 201
            assert response.json()["id"] == 123

See Also:
    - BaseAiohttpTestCases: Base class for aiohttp test utilities.
    - BaseRequestsTestCases: Base class for requests test utilities.
    - BaseUrllib3TestCases: Base class for urllib3 test utilities.
"""

from functools import wraps
from typing import Any, Dict, Optional
from unittest.mock import AsyncMock, Mock, patch

from .aiohttp_ import BaseAiohttpTestCases
from .requests_ import BaseRequestsTestCases
from .urllib3_ import BaseUrllib3TestCases


def patch_aiohttp(
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
):
    """
    Decorator that patches `aiohttp.ClientSession._request` with
    an `AsyncMock`. This decorator works with both async test functions
    and sync functions using `asyncio.run()`. It automatically creates
    a mock response with the specified parameters and patches
    the `aiohttp` client session.

    Args:
        url: The URL that the mock should respond to. Defaults to "https://example.com".
        method: HTTP method for the mock request. Defaults to "GET".
        json_response: JSON data to return in the response body. Mutually exclusive with text_response and content.
        status: HTTP status code for the mock response. Defaults to 200.
        headers: Dictionary of response headers.
        text_response: Plain text data to return. Mutually exclusive with json_response and content.
        content: Raw bytes to return as response content. Mutually exclusive with json_response and text_response.
        content_type: MIME type of the response. Defaults to "application/json".
        charset: Character encoding for the response. Defaults to "utf-8".
        raise_for_status_exception: Exception to raise when response.raise_for_status() is called.

    Returns:
        Decorated function that runs with mocked aiohttp requests.

    Example:
        Basic JSON response mocking::

            @patch_aiohttp(json_response={"id": 123}, status=201)
            def test_aiohttp_mock_json(self):
                async def test():
                    async with aiohttp.ClientSession() as session:
                        async with session.get("https://example.com") as resp:
                            self.assertEqual(resp.status, 201)
                            self.assertEqual(await resp.json(), {"id": 123})

                asyncio.run(test())

        Error simulation::

            @patch_aiohttp(status=404, raise_for_status_exception=aiohttp.ClientResponseError(...))
            def test_error_handling(self):
                # Test error handling logic
                pass

    Note:
        This decorator patches the private method `_request` which may change between
        aiohttp versions. Consider pinning aiohttp version in your requirements.
    """

    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            mock_response = BaseAiohttpTestCases.get_aiohttp_mock(
                url=url,
                method=method,
                json_response=json_response,
                status=status,
                headers=headers,
                text_response=text_response,
                content=content,
                content_type=content_type,
                charset=charset,
                raise_for_status_exception=raise_for_status_exception,
            )

            with patch(
                target="aiohttp.client.ClientSession._request",
                new_callable=lambda: AsyncMock(return_value=mock_response),
            ):
                return func(*args, **kwargs)

        return wrapper

    return decorator


def patch_requests(
    url: str = "https://example.com",
    encoding: str = "utf-8",
    headers: Optional[Dict[str, str]] = None,
    json_response: Optional[Dict[str, Any]] = None,
    text_response: Optional[str] = None,
    status_code: int = 200,
    content: Optional[bytes] = None,
    raise_for_status_exception: Optional[Exception] = None,
):
    """
    Decorator that patches requests.sessions.Session.request to
    return mock responses. This decorator simplifies testing code
    that uses the `requests` library by automatically patching
    the HTTP requests and returning configurable mock
    responses.

    Args:
        url: The URL that the mock should respond to. Defaults to "https://example.com".
        encoding: Character encoding for the response. Defaults to "utf-8".
        headers: Dictionary of response headers.
        json_response: JSON data to return in the response body. Mutually exclusive with text_response and content.
        text_response: Plain text data to return. Mutually exclusive with json_response and content.
        status_code: HTTP status code for the mock response. Defaults to 200.
        content: Raw bytes to return as response content. Mutually exclusive with json_response and text_response.
        raise_for_status_exception: Exception to raise when response.raise_for_status() is called.

    Returns:
        Decorated function that runs with mocked requests.

    Example:
        Basic JSON response::

            @patch_requests(json_response={"id": 1})
            def test_get_request_mock_json(self):
                response = requests.get("https://example.com")
                self.assertEqual(response.json(), {"id": 1})

        Custom status code and headers::

            @patch_requests(
                status_code=201,
                headers={"Location": "/api/users/123"},
                json_response={"created": True}
            )
            def test_post_creation(self):
                response = requests.post("https://api.example.com/users")
                self.assertEqual(response.status_code, 201)
                self.assertEqual(response.headers["Location"], "/api/users/123")

        Error handling::

            @patch_requests(
                status_code=400,
                raise_for_status_exception=requests.HTTPError("Bad Request")
            )
            def test_error_handling(self):
                response = requests.get("https://example.com")
                with self.assertRaises(requests.HTTPError):
                    response.raise_for_status()
    """

    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            with patch(
                target="requests.sessions.Session.request",
                return_value=BaseRequestsTestCases.get_requests_mock(
                    url=url,
                    encoding=encoding,
                    headers=headers,
                    json_response=json_response,
                    text_response=text_response,
                    status_code=status_code,
                    content=content,
                    raise_for_status_exception=raise_for_status_exception,
                ),
            ):
                return func(*args, **kwargs)

        return wrapper

    return decorator


def patch_urllib3(
    url: str = "https://example.com",
    method: str = "GET",
    status: int = 200,
    data: bytes = b'{"message": "success"}',
    headers: Optional[Dict[str, str]] = None,
    reason: Optional[str] = None,
    version: int = 11,
    preload_content: bool = True,
    decode_content: bool = True,
    version_string: str = "HTTP/1.1",
    original_response: Optional[Mock] = None,
    pool: Optional[Mock] = None,
    connection: Optional[Mock] = None,
    msg: Optional[Mock] = None,
    retries: Optional[Mock] = None,
    enforce_content_length: bool = False,
    with_json_attr: bool = True,
):
    """
    Decorator that patches urllib3 requests to return mock
    responses. This decorator provides comprehensive mocking for `urllib3`,
    the low-level HTTP library used by `requests`. It offers fine-grained
    control over response properties including connection details
    and HTTP protocol specifics.

    Args:
        url: The URL that the mock should respond to. Defaults to "https://example.com".
        method: HTTP method for the mock request. Defaults to "GET".
        status: HTTP status code for the mock response. Defaults to 200.
        data: Raw bytes to return as response data. Defaults to b'{"message": "success"}'.
        headers: Dictionary of response headers.
        reason: HTTP status reason phrase (e.g., "OK", "Not Found").
        version: HTTP version as integer (11 for HTTP/1.1, 20 for HTTP/2.0). Defaults to 11.
        preload_content: Whether response content is preloaded. Defaults to True.
        decode_content: Whether to decode content based on Content-Encoding. Defaults to True.
        version_string: HTTP version string representation. Defaults to "HTTP/1.1".
        original_response: Mock of the original response object.
        pool: Mock of the connection pool.
        connection: Mock of the HTTP connection.
        msg: Mock of the HTTP message object.
        retries: Mock of the retry configuration.
        enforce_content_length: Whether to enforce Content-Length header. Defaults to False.
        with_json_attr: Whether to add a json() method to the response. Defaults to True.

    Returns:
        Decorated function that runs with mocked urllib3 requests.

    Example:
        Basic usage::

            @patch_urllib3(status=404, data=b'{"error": "not found"}')
            def test_urllib3_mock_404(self):
                http = urllib3.PoolManager()
                response = http.request("GET", "https://example.com")
                self.assertEqual(response.status, 404)
                self.assertEqual(response.data, b'{"error": "not found"}')

        Advanced configuration::

            @patch_urllib3(
                status=200,
                data=b'{"users": []}',
                headers={"Content-Type": "application/json", "X-Total-Count": "0"},
                version=20,  # HTTP/2.0
                version_string="HTTP/2.0"
            )
            def test_http2_response(self):
                http = urllib3.PoolManager()
                response = http.request("GET", "https://api.example.com/users")
                self.assertEqual(response.status, 200)
                self.assertEqual(response.headers["X-Total-Count"], "0")

        JSON response with convenience method::

            @patch_urllib3(data=b'{"id": 123}', with_json_attr=True)
            def test_json_response(self):
                http = urllib3.PoolManager()
                response = http.request("GET", "https://example.com")
                self.assertEqual(response.json(), {"id": 123})

    Note:
        This decorator patches internal urllib3 methods which may change between
        versions. The extensive parameter list provides maximum flexibility for
        testing edge cases and low-level HTTP behavior.
    """

    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            with patch(
                target="urllib3._request_methods.RequestMethods.request",
                return_value=BaseUrllib3TestCases.get_urllib3_mock(
                    url=url,
                    method=method,
                    status=status,
                    data=data,
                    headers=headers,
                    reason=reason,
                    version=version,
                    preload_content=preload_content,
                    decode_content=decode_content,
                    version_string=version_string,
                    original_response=original_response,
                    pool=pool,
                    connection=connection,
                    msg=msg,
                    retries=retries,
                    enforce_content_length=enforce_content_length,
                    with_json_attr=with_json_attr,
                ),
            ):
                return func(*args, **kwargs)

        return wrapper

    return decorator
