# -*- coding: utf-8 -*-

"""
Test utilities for urllib3 HTTP client library.

This module provides specialized test case utilities for testing code that uses
urllib3, the low-level HTTP library that powers requests. It extends the base HTTP
test functionality with urllib3-specific mock objects and response simulation.

Key features:
- Comprehensive HTTPResponse mock objects with full urllib3 API support
- Streaming and chunked response simulation
- HTTP/1.1 and HTTP/2.0 version support
- Connection pool and retry mechanism mocking
- Low-level socket-like reading methods (read, read1, readinto, etc.)
- HTTPHeaderDict integration for case-insensitive headers

Example:
    Basic urllib3 response mocking::

        from core_https.tests.urllib3_ import BaseUrllib3TestCases

        class MyUrllib3Test(BaseUrllib3TestCases):
            def test_http_response(self):
                mock_response = self.get_urllib3_mock(
                    data=b'{"users": ["alice", "bob"]}',
                    status=200,
                    headers={"Content-Type": "application/json"}
                )

                # Test urllib3-specific methods
                self.assertEqual(mock_response.status, 200)
                self.assertEqual(mock_response.json(), {"users": ["alice", "bob"]})
                self.assertIsInstance(mock_response.headers, HTTPHeaderDict)

Note:
    This module creates very comprehensive mocks that simulate most urllib3.HTTPResponse
    features. The complexity is necessary to support urllib3's extensive low-level API.

See Also:
    - BaseHttpTestCases: Base class for HTTP testing utilities
    - BaseRequestsTestCases: Test utilities for requests library
    - BaseAiohttpTestCases: Test utilities for aiohttp library
"""

import json
from typing import Dict, Optional
from unittest.mock import Mock

from urllib3._collections import HTTPHeaderDict

from core_https.tests.base import BaseHttpTestCases


class BaseUrllib3TestCases(BaseHttpTestCases):
    """
    Test utilities for urllib3 HTTP client library.

    This class provides specialized methods for creating mock urllib3.HTTPResponse
    objects that closely simulate the behavior of real urllib3 responses. It extends
    BaseHttpTestCases with urllib3-specific functionality including streaming,
    connection management, and low-level socket operations.

    The class creates comprehensive mocks with extensive parameter control to support
    testing of code that relies on urllib3's low-level HTTP functionality.

    Example:
        Creating comprehensive urllib3 response mocks::

            class MyUrllib3Test(BaseUrllib3TestCases):
                def test_streaming_response(self):
                    mock = self.get_urllib3_mock(
                        data=b"chunk1\\nchunk2\\nchunk3",
                        status=200,
                        preload_content=False
                    )

                    # Test streaming methods
                    chunks = list(mock.stream(chunk_size=10))
                    self.assertGreater(len(chunks), 0)

                def test_http2_response(self):
                    mock = self.get_urllib3_mock(
                        status=200,
                        version=20,
                        version_string="HTTP/2.0"
                    )

                    self.assertEqual(mock.version, 20)
                    self.assertEqual(mock.version_string, "HTTP/2.0")

        Testing low-level socket operations::

            def test_socket_methods(self):
                data = b"Hello, World!"
                mock = self.get_urllib3_mock(data=data)

                # Test socket-like reading methods
                buffer = bytearray(5)
                bytes_read = mock.readinto(buffer)
                self.assertEqual(bytes_read, 5)
                self.assertEqual(buffer, b"Hello")

    Note:
        The urllib3 mocks are the most comprehensive in this test suite due to
        urllib3's extensive low-level API. They include socket-like methods,
        streaming support, and connection management features.
    """

    @classmethod
    def get_urllib3_mock(
        cls,
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
    ) -> Mock:
        """
        Create a comprehensive mock urllib3.HTTPResponse object for testing.

        This method creates a highly detailed mock that simulates urllib3's HTTPResponse
        behavior including streaming, connection management, and low-level socket operations.
        It supports both HTTP/1.1 and HTTP/2.0 protocols with extensive customization options.

        Args:
            url: The URL that the mock response represents. Defaults to "https://example.com".
            method: HTTP method for the request. Defaults to "GET".
            status: HTTP status code for the response. Defaults to 200.
            data: Raw bytes content of the response body. Defaults to b'{"message": "success"}'.
            headers: Dictionary of response headers (case-insensitive via HTTPHeaderDict).
            reason: HTTP status reason phrase. Auto-generated from status code if not provided.
            version: HTTP version as integer (11 for HTTP/1.1, 20 for HTTP/2.0). Defaults to 11.
            preload_content: Whether response content is preloaded. Affects streaming behavior.
            decode_content: Whether to decode content based on Content-Encoding headers.
            version_string: HTTP version string representation. Defaults to "HTTP/1.1".
            original_response: Mock of the original raw response object.
            pool: Mock of the urllib3 connection pool.
            connection: Mock of the underlying HTTP connection.
            msg: Mock of the HTTP message object (httplib.HTTPMessage).
            retries: Mock of the retry configuration object.
            enforce_content_length: Whether to enforce Content-Length header validation.
            with_json_attr: Whether to include a json() method for convenience. Defaults to True.

        Returns:
            Mock object simulating urllib3.HTTPResponse with comprehensive API support.

        Example:
            Basic HTTP response mock::

                mock_response = BaseUrllib3TestCases.get_urllib3_mock(
                    data=b'{"users": ["alice", "bob"]}',
                    status=200,
                    headers={"Content-Type": "application/json"}
                )

                # Test standard response properties
                self.assertEqual(mock_response.status, 200)
                self.assertEqual(mock_response.json()["users"], ["alice", "bob"])
                self.assertIsInstance(mock_response.headers, HTTPHeaderDict)

            Streaming response simulation::

                stream_mock = BaseUrllib3TestCases.get_urllib3_mock(
                    data=b"chunk1\\nchunk2\\nchunk3",
                    preload_content=False
                )

                # Test streaming methods
                chunks = list(stream_mock.stream(chunk_size=10))
                lines = stream_mock.readlines()
                self.assertGreater(len(chunks), 0)

            HTTP/2.0 response::

                http2_mock = BaseUrllib3TestCases.get_urllib3_mock(
                    status=200,
                    version=20,
                    version_string="HTTP/2.0",
                    headers={"server": "nginx/1.20"}
                )

                self.assertEqual(http2_mock.version, 20)
                self.assertEqual(http2_mock.version_string, "HTTP/2.0")

            Socket-like operations::

                socket_mock = BaseUrllib3TestCases.get_urllib3_mock(
                    data=b"Hello, World!"
                )

                # Test low-level reading methods
                buffer = bytearray(5)
                bytes_read = socket_mock.readinto(buffer)
                self.assertEqual(bytes_read, 5)
                self.assertEqual(bytes(buffer), b"Hello")

                # Test line-by-line reading
                line = socket_mock.readline()
                self.assertIsInstance(line, bytes)

        Note:
            This mock provides extensive urllib3.HTTPResponse API compatibility including:
            - Standard attributes (status, headers, data, etc.)
            - Socket-like reading methods (read, read1, readinto, readline, readlines)
            - Streaming support (stream method with chunking)
            - Context manager protocol (__enter__, __exit__)
            - Iterator protocol for line-by-line reading
            - Header access methods (getheader, getheaders)
            - Connection management (close, release_conn)
            - JSON convenience method (if with_json_attr=True)

            The complexity of this mock reflects urllib3's comprehensive low-level HTTP API.
        """

        if headers is None:
            headers = {"Content-Type": "application/json"}

        if reason is None:
            reason = cls.code_mapper.get(status)

        mock = Mock()

        mock.url = url
        mock._request_url = url
        mock.status = status

        mock.reason = reason
        mock.version_string = version_string
        mock.version = version

        mock.data = data if preload_content else None
        mock._body = data if preload_content else None
        mock.decode_content = decode_content

        # Headers - urllib3 uses HTTPHeaderDict
        header_dict = HTTPHeaderDict(headers)
        mock.headers = header_dict
        mock.msg = msg or Mock()

        # Request information
        mock.request_method = method

        # Connection and pool info...
        mock._original_response = original_response
        mock._pool = pool
        mock._connection = connection
        mock.retries = retries
        mock.enforce_content_length = enforce_content_length

        # Content handling flags...
        mock.closed = Mock(return_value=False)
        mock.readable = Mock(return_value=True)

        # Methods for reading content...
        def mock_read(amt=None, decode_content=None):
            """Mock read method."""
            if preload_content:
                return data.decode() if decode_content else data
            else:
                # Simulate streaming read...
                res = data[:amt] if amt else data
                return res.decode() if decode_content else res

        def mock_read1(amt=None):
            """Mock read1 method (reads up to amt bytes)."""
            return mock_read(amt)

        def mock_readinto(b):
            """Mock readinto method."""
            info = data[: len(b)]
            b[: len(info)] = info
            return len(info)

        def mock_readline(size=-1):
            lines = data.split(b"\n", 1)
            line = lines[0] + b"\n" if len(lines) > 1 else lines[0]
            return line[:size] if size > 0 else line

        def mock_readlines(hint=-1):
            return data.split(b"\n")

        # Assign read methods...
        mock.read = mock_read
        mock.read1 = mock_read1
        mock.readinto = mock_readinto
        mock.readline = mock_readline
        mock.readlines = mock_readlines

        # Stream methods
        def mock_stream(amt=2**16, decode_content=None):
            if not data:
                return

            chunk_size = amt or 2**16
            for i in range(0, len(data), chunk_size):
                yield data[i : i + chunk_size]

        mock.stream = mock_stream

        # Header methods...
        def mock_getheaders():
            return HTTPHeaderDict(header_dict)

        def mock_getheader(name, default=None):
            return header_dict.get(name, default)

        mock.getheaders = mock_getheaders
        mock.getheader = mock_getheader

        # Connection management
        def mock_close():
            """Mock close method."""
            mock.closed.return_value = True
            mock.readable.return_value = False

        def mock_release_conn():
            """Mock release_conn method."""

        mock.close = mock_close
        mock.release_conn = mock_release_conn

        # Context manager support
        mock.__enter__ = Mock(return_value=mock)
        mock.__exit__ = Mock(side_effect=mock_close())

        # Iterator support
        def mock_iter(self):
            """Support for iteration over response."""
            yield from data.split(b"\n")

        mock.__iter__ = mock_iter

        def mock_json():
            return json.loads(data.decode("utf-8"))

        mock.json = mock_json
        if not with_json_attr:
            delattr(mock, "json")

        return mock
