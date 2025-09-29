# -*- coding: utf-8 -*-

"""
HTTP client exception hierarchy for the core_https library.

This module provides a comprehensive set of exception classes for handling
HTTP-related errors in a structured and consistent manner. The exception
hierarchy is designed to allow for fine-grained error handling while
maintaining compatibility with standard HTTP status codes.

Exception Hierarchy:
    Exception
    └── InternalServerError (base for all HTTP errors)
        ├── ServiceException (handled service errors)
        │   ├── AuthenticationException (401 Unauthorized)
        │   ├── AuthorizationException (403 Forbidden)
        │   └── RateLimitException (429 Too Many Requests)
        └── RetryableException (errors that should trigger retries)

Usage Example:
    Basic exception handling::

        from core_https.exceptions import AuthenticationException, RateLimitException

        try:
            response = requester.request(url="https://api.example.com")
        except AuthenticationException as e:
            logger.error(f"Authentication failed: {e.details}")
            # Handle authentication error
        except RateLimitException as e:
            logger.warning(f"Rate limited: {e.details}")
            # Implement backoff strategy
        except ServiceException as e:
            logger.error(f"Service error {e.status_code}: {e.details}")
            # Handle other service errors

    Error information extraction::

        try:
            # HTTP request that fails
            pass
        except InternalServerError as e:
            error_info = e.get_error_info()
            # {'type': 'AuthenticationException', 'details': 'Invalid API key'}

See Also:
    - core_https.requesters.base.IRequester: Base requester that raises these exceptions
    - HTTP status codes: https://developer.mozilla.org/en-US/docs/Web/HTTP/Status
"""

from typing import Dict


class InternalServerError(Exception):
    """
    Base class for all HTTP-related exceptions in the core_https library.

    This exception serves as the root of the HTTP exception hierarchy and handles
    unhandled errors that occur during HTTP operations. It provides structured
    error information including HTTP status codes and detailed error messages.

    Attributes:
        status_code: HTTP status code associated with the error
        details: Detailed error message or description
    """

    def __init__(
        self,
        status_code: int,
        details: str,
        *args,
    ) -> None:
        super().__init__(*args)
        self.status_code = status_code
        self.details = details

    def get_error_info(self) -> Dict[str, str]:
        """
        Get structured error information for logging or serialization.
        :returns: Dictionary containing error type and details.
        """

        return {
            "type": self.__class__.__name__,
            "details": self.details,
        }


class ServiceException(InternalServerError):
    """Exception caused for handled errors within the service"""


class AuthenticationException(ServiceException):
    """Exception caused for authentication [401] issues"""

    def __init__(
        self,
        status_code: int = 401,
        details: str = "Unauthorized",
    ) -> None:
        super().__init__(
            status_code=status_code,
            details=details,
        )


class AuthorizationException(ServiceException):
    """Exception caused for authorization [403] issues"""

    def __init__(
        self,
        status_code: int = 403,
        details: str = "Forbidden",
    ) -> None:
        super().__init__(
            status_code=status_code,
            details=details,
        )


class RateLimitException(ServiceException):
    """
    Exception caused [429] when a client has sent too many requests
    to a server within a given time frame.
    """

    def __init__(
        self,
        status_code: int = 429,
        details: str = "Too Many Requests",
    ) -> None:
        super().__init__(
            status_code=status_code,
            details=details,
        )


class RetryableException(InternalServerError):
    """
    Exception for HTTP errors that should trigger retry mechanisms.

    This exception represents temporary failures that are likely to succeed
    if retried after a short delay. Common retryable status codes include:
    - 429 Too Many Requests (rate limiting)
    - 502 Bad Gateway (temporary server issue)
    - 503 Service Unavailable (server overload)
    - 504 Gateway Timeout (temporary timeout)

    Example:
        raise RetryableException(status_code=503, details="Service temporarily unavailable")
        raise RetryableException(status_code=502, details="Bad gateway from upstream")
    """
