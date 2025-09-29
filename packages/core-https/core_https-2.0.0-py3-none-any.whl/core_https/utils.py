# -*- coding: utf-8 -*-

"""
HTTP utilities for the core_https library.

This module provides HTTP constants and utilities that maintain backward
compatibility with older Python versions. It includes comprehensive HTTP
status codes and methods that match the standard library implementations
introduced in Python 3.11.

Key features:
- Complete HTTP status code enumeration with descriptions
- Standard HTTP method definitions with documentation
- Backward compatibility with Python < 3.11
- Utility methods for status code and method lookup
- Type-safe enum implementations

Example:
    Basic usage of HTTP status codes::

        from core_https.utils import HTTPStatus, HTTPMethod

        # Access status codes
        print(HTTPStatus.OK.code)          # 200
        print(HTTPStatus.OK.description)   # "OK"

        # Find status by code
        status = HTTPStatus.by_code(404)
        print(status.description)          # "Not Found"

        # Get all status codes as dictionary
        status_map = HTTPStatus.as_dict()
        # {200: "OK", 404: "Not Found", ...}

    HTTP methods usage::

        # Access HTTP methods
        print(HTTPMethod.GET.value)        # "GET"
        print(HTTPMethod.POST.description) # "Perform resource-specific processing..."

        # Find method by name
        method = HTTPMethod.by_name("patch")
        print(method.value)                # "PATCH"

See Also:
    - HTTP/1.1 Status Codes: https://tools.ietf.org/html/rfc7231#section-6
    - HTTP Methods: https://tools.ietf.org/html/rfc7231#section-4
"""

from enum import Enum
from typing import Dict

try:
    from typing import Self

except ImportError:
    # For earlier versions...
    from typing_extensions import Self


class HTTPStatus(Enum):
    """
    HTTP status code enumeration with backward compatibility.

    This enum provides comprehensive HTTP status codes with their standard
    descriptions. It maintains compatibility with Python versions prior to 3.11
    where http.HTTPStatus was introduced.

    Each status code includes both the numeric code and the standard description
    as defined in RFC specifications.

    Attributes:
        `code`: The numeric HTTP status code (e.g., 200, 404, 500)
        `description`: The standard description for the status code

    Example:
        Using HTTP status codes::

            # Access specific status codes
            status = HTTPStatus.OK
            print(f"Code: {status.code}")           # Code: 200
            print(f"Description: {status.description}")  # Description: OK

            # Find status by code
            not_found = HTTPStatus.by_code(404)
            print(not_found.description)           # Not Found

            # Check if status indicates success
            if HTTPStatus.CREATED.is_success():
                print("Request succeeded!")

            # Get all status codes
            all_codes = HTTPStatus.as_dict()
            # {100: 'Continue', 200: 'OK', 404: 'Not Found', ...}
    """

    CONTINUE = 100, "Continue"
    SWITCHING_PROTOCOLS = 101, "Switching Protocols"
    PROCESSING = 102, "Processing"
    EARLY_HINTS = 103, "Early Hints"

    OK = 200, "OK"
    CREATED = 201, "Created"
    ACCEPTED = 202, "Accepted"
    NON_AUTHORITATIVE_INFORMATION = 203, "Non-Authoritative Information"
    NO_CONTENT = 204, "No Content"
    RESET_CONTENT = 205, "Reset Content"
    PARTIAL_CONTENT = 206, "Partial Content"
    MULTI_STATUS = 207, "Multi-Status"
    ALREADY_REPORTED = 208, "Already Reported"
    IM_USED = 226, "IM Used"

    MULTIPLE_CHOICES = 300, "Multiple Choices"
    MOVED_PERMANENTLY = 301, "Moved Permanently"
    FOUND = 302, "Found"
    SEE_OTHER = 303, "See Other"
    NOT_MODIFIED = 304, "Not Modified"
    USE_PROXY = 305, "Use Proxy"
    TEMPORARY_REDIRECT = 307, "Temporary Redirect"
    PERMANENT_REDIRECT = 308, "Permanent Redirect"

    BAD_REQUEST = 400, "Bad Request"
    UNAUTHORIZED = 401, "Unauthorized"
    PAYMENT_REQUIRED = 402, "Payment Required"
    FORBIDDEN = 403, "Forbidden"
    NOT_FOUND = 404, "Not Found"
    METHOD_NOT_ALLOWED = 405, "Method Not Allowed"
    NOT_ACCEPTABLE = 406, "Not Acceptable"
    PROXY_AUTHENTICATION_REQUIRED = 407, "Proxy Authentication Required"
    REQUEST_TIMEOUT = 408, "Request Timeout"
    CONFLICT = 409, "Conflict"
    GONE = 410, "Gone"
    LENGTH_REQUIRED = 411, "Length Required"
    PRECONDITION_FAILED = 412, "Precondition Failed"
    PAYLOAD_TOO_LARGE = 413, "Payload Too Large"
    URI_TOO_LONG = 414, "URI Too Long"
    UNSUPPORTED_MEDIA_TYPE = 415, "Unsupported Media Type"
    RANGE_NOT_SATISFIABLE = 416, "Range Not Satisfiable"
    EXPECTATION_FAILED = 417, "Expectation Failed"
    IM_A_TEAPOT = 418, "I'm a teapot"
    MISDIRECTED_REQUEST = 421, "Misdirected Request"
    UNPROCESSABLE_ENTITY = 422, "Unprocessable Entity"
    LOCKED = 423, "Locked"
    FAILED_DEPENDENCY = 424, "Failed Dependency"
    TOO_EARLY = 425, "Too Early"
    UPGRADE_REQUIRED = 426, "Upgrade Required"
    PRECONDITION_REQUIRED = 428, "Precondition Required"
    TOO_MANY_REQUESTS = 429, "Too Many Requests"
    REQUEST_HEADER_FIELDS_TOO_LARGE = 431, "Request Header Fields Too Large"
    UNAVAILABLE_FOR_LEGAL_REASONS = 451, "Unavailable For Legal Reasons"

    INTERNAL_SERVER_ERROR = 500, "Internal Server Error"
    NOT_IMPLEMENTED = 501, "Not Implemented"
    BAD_GATEWAY = 502, "Bad Gateway"
    SERVICE_UNAVAILABLE = 503, "Service Unavailable"
    GATEWAY_TIMEOUT = 504, "Gateway Timeout"
    HTTP_VERSION_NOT_SUPPORTED = 505, "HTTP Version Not Supported"
    VARIANT_ALSO_NEGOTIATES = 506, "Variant Also Negotiates"
    INSUFFICIENT_STORAGE = 507, "Insufficient Storage"
    LOOP_DETECTED = 508, "Loop Detected"
    NOT_EXTENDED = 510, "Not Extended"
    NETWORK_AUTHENTICATION_REQUIRED = 511, "Network Authentication Required"

    def __init__(self, code, description):
        """Initialize HTTP status with code and description."""
        self._value_ = code
        self._description = description

    def __repr__(self):
        """Return string representation for debugging."""
        return f"<{self.__class__.__name__}.{self._value_}>"

    def __str__(self):
        """Return string representation of the status code."""
        return str(self.value)

    @property
    def code(self):
        """Get the numeric HTTP status code."""
        return self._value_

    @property
    def description(self):
        """Get the standard description for this status code."""
        return self._description

    def is_informational(self) -> bool:
        """Check if status code is informational (1xx)."""
        return 100 <= self.code < 200

    def is_success(self) -> bool:
        """Check if status code indicates success (2xx)."""
        return 200 <= self.code < 300

    def is_redirection(self) -> bool:
        """Check if status code indicates redirection (3xx)."""
        return 300 <= self.code < 400

    def is_client_error(self) -> bool:
        """Check if status code indicates client error (4xx)."""
        return 400 <= self.code < 500

    def is_server_error(self) -> bool:
        """Check if status code indicates server error (5xx)."""
        return 500 <= self.code < 600

    def is_error(self) -> bool:
        """Check if status code indicates any error (4xx or 5xx)."""
        return self.is_client_error() or self.is_server_error()

    @classmethod
    def by_code(cls, code: int) -> Self:
        """
        Find HTTP status by numeric code.

        Args:
            code: The numeric HTTP status code to look up

        Returns:
            HTTPStatus instance for the given code

        Raises:
            ValueError: If no status code matches the given code

        Example:
            status = HTTPStatus.by_code(404)
            print(status.description)  # "Not Found"
        """

        for status in cls:
            if status.value == code:
                return status

        raise ValueError(f"No HTTPStatus found for code: {code}")

    @classmethod
    def as_dict(cls) -> Dict[int, str]:
        """
        Get all HTTP status codes as a dictionary.

        Returns:
            Dictionary mapping status codes to descriptions

        Example:
            codes = HTTPStatus.as_dict()
            print(codes[200])  # "OK"
        """

        return {
            member.code: member.description
            for member in cls
        }


class HTTPMethod(Enum):
    """
    HTTP method enumeration with backward compatibility.

    This enum provides standard HTTP methods with their descriptions. It maintains
    compatibility with Python versions prior to 3.11 where http.HTTPMethod was
    introduced.

    Each method includes the string name and a description of its intended purpose
    as defined in HTTP specifications.

    Example:
        Using HTTP methods::

            # Access methods
            method = HTTPMethod.GET
            print(method.value)        # "GET"
            print(method.description)  # "Retrieve the resource."

            # Find method by string name
            post = HTTPMethod.by_name("post")  # Case insensitive
            print(post.value)          # "POST"

            # Check method properties
            if HTTPMethod.POST.is_idempotent():
                print("POST is idempotent")  # This won't print

            if HTTPMethod.GET.is_safe():
                print("GET is safe")     # This will print
    """

    CONNECT = "CONNECT", "Establish a connection to the server."
    DELETE = "DELETE", "Delete the resource."
    GET = "GET", "Retrieve the resource."
    HEAD = "HEAD", "Same as GET, but only retrieve the status line and header section."
    OPTIONS = "OPTIONS", "Describe the communication options for the resource."
    PATCH = "PATCH", "Apply partial modifications to a resource."
    POST = "POST", "Perform resource-specific processing with the request payload."
    PUT = "PUT", "Replace the resource with the request payload."
    TRACE = "TRACE", "Perform a message loop-back test along the path to the resource."

    def __init__(self, name: str, description: str):
        """Initialize HTTP method with name and description."""
        self._value_ = name
        self._description = description

    def __repr__(self):
        """Return string representation for debugging."""
        return f"<{self.__class__.__name__}.{self._value_}>"

    def __str__(self):
        """Return string representation of the method name."""
        return self._value_

    @property
    def description(self):
        """Get the description of this HTTP method."""
        return self._description

    def is_safe(self) -> bool:
        """
        Check if method is considered safe (read-only).

        Safe methods are those that do not modify server state.
        """
        return self in (HTTPMethod.GET, HTTPMethod.HEAD, HTTPMethod.OPTIONS, HTTPMethod.TRACE)

    def is_idempotent(self) -> bool:
        """
        Check if method is idempotent.

        Idempotent methods can be called multiple times with the same result.
        """
        return self in (HTTPMethod.GET, HTTPMethod.HEAD, HTTPMethod.PUT, HTTPMethod.DELETE,
                       HTTPMethod.OPTIONS, HTTPMethod.TRACE)

    def is_cacheable(self) -> bool:
        """
        Check if responses to this method are typically cacheable.

        Note: Cacheability also depends on response headers.
        """
        return self in (HTTPMethod.GET, HTTPMethod.HEAD, HTTPMethod.POST)

    @classmethod
    def by_name(cls, name: str) -> Self:
        """
        Find HTTP method by name (case-insensitive).

        Args:
            name: The HTTP method name to look up

        Returns:
            HTTPMethod instance for the given name

        Raises:
            ValueError: If no method matches the given name

        Example:
            method = HTTPMethod.by_name("get")  # Case insensitive
            print(method.value)  # "GET"
        """

        name = name.upper()

        for http_method in cls:
            if http_method.value == name:
                return http_method

        raise ValueError(f"No HTTPMethod found for name: {name}")
