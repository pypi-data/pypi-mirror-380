# -*- coding: utf-8 -*-

import re
from abc import ABC
from abc import abstractmethod
from typing import Any, Dict, Optional

from core_mixins.interfaces.factory import IFactory

from core_https.exceptions import (
    AuthenticationException,
    AuthorizationException,
    InternalServerError,
    RateLimitException,
    RetryableException,
    ServiceException,
)

try:
    from http import HTTPMethod as _HTTPMethod
except ImportError:
    from core_https.utils import HTTPMethod as _HTTPMethod  # type: ignore


# Type alias that works with both standard library
# and the custom HTTPMethod...
HTTPMethod = _HTTPMethod


class IRequester(IFactory, ABC):
    """
    Abstract base interface for HTTP requesters with comprehensive configuration and error handling.

    This abstract class defines the standard interface for all HTTP requester implementations
    in the core_https library. It provides a factory pattern for creating requester instances,
    comprehensive parameter validation, encoding detection, and standardized exception mapping.

    All concrete implementations must inherit from this class and implement the abstract
    methods: engine() and request(). The class supports various HTTP libraries through
    a pluggable architecture while maintaining consistent behavior and error handling.

    Features:
        - Factory pattern for requester instantiation
        - Comprehensive parameter validation with clear error messages
        - Automatic encoding detection from HTTP response headers
        - Standardized HTTP exception mapping (401→AuthenticationException, etc.)
        - Configurable connection pooling and timeouts
        - Support for retry strategies and backoff factors

    Parameters:
        encoding: Character encoding for response decoding. Defaults to "utf-8".
            Must be a non-empty string after stripping whitespace.

        raise_for_status: Whether to automatically raise exceptions for HTTP error status codes.
            When True, 4xx and 5xx responses will raise appropriate exceptions.

        retries: Retry strategy configuration. Can be an integer for simple retry counts
            or a library-specific retry object (e.g., urllib3.util.retry.Retry).
            Different implementations may handle this parameter differently.

        backoff_factor: Exponential backoff multiplier between retry attempts.
            Must be non-negative. The actual delay is typically: backoff_factor * attempt_number.

        connector_limit: Maximum number of connections in the connection pool.
            Must be positive and greater than or equal to connector_limit_per_host.

        connector_limit_per_host: Maximum connections per individual host.
            Must be positive and cannot exceed connector_limit.

        timeout: Request timeout in seconds. Must be positive and should not exceed 3600 seconds.
            Individual requests may override this value based on implementation.

    See Also:
        - :class:`core_https.requesters.aiohttp_.AioHttpRequester`: Async implementation
        - :class:`core_https.requesters.requests_.RequestsRequester`: Synchronous implementation
        - :class:`core_https.requesters.urllib3_.Urllib3Requester`: Low-level implementation
        - :class:`core_mixins.interfaces.factory.IFactory`: Base factory interface
    """

    def __init__(
        self,
        encoding: str = "utf-8",
        raise_for_status: bool = False,
        retries: Optional[Any] = None,
        backoff_factor: Optional[float] = None,
        connector_limit: int = 100,
        connector_limit_per_host: int = 30,
        timeout: int = 10,
    ) -> None:
        """
        Initialize the HTTP requester with validated configuration parameters.

        This constructor performs comprehensive validation on all input parameters
        to ensure they meet the required constraints. Invalid parameters will
        raise ValueError with descriptive error messages.

        Args:
            encoding: Character encoding for response decoding. Must be a non-empty
                string after stripping whitespace. Defaults to "utf-8".
                Common values: "utf-8", "iso-8859-1", "windows-1252".

            raise_for_status: Whether to automatically raise exceptions for HTTP
                error status codes. When True, responses with 4xx or 5xx status
                codes will raise appropriate exceptions instead of returning normally.

            retries: Retry strategy configuration. Can be None (no retries),
                an integer (simple retry count), or a library-specific retry
                object (e.g., urllib3.util.retry.Retry). Different implementations
                may interpret this parameter differently.

            backoff_factor: Exponential backoff multiplier for retry delays.
                Must be non-negative. The actual delay between retries is typically
                calculated as: backoff_factor * attempt_number seconds.
                Use None to disable backoff delays.

            connector_limit: Maximum number of concurrent connections in the
                connection pool. Must be positive and >= connector_limit_per_host.
                Higher values allow more concurrent requests but use more resources.

            connector_limit_per_host: Maximum concurrent connections per individual
                host/domain. Must be positive and <= connector_limit. This prevents
                overwhelming any single server with too many concurrent connections.

            timeout: Default request timeout in seconds. Must be positive and
                should not exceed 3600 seconds (1 hour). Individual requests may
                override this value depending on the implementation.

        Raises:
            ValueError: If any parameter violates its constraints:
                - encoding is empty or whitespace-only
                - backoff_factor is negative
                - timeout is zero, negative, or > 3600 seconds
                - connector_limit or connector_limit_per_host are zero or negative
                - connector_limit_per_host exceeds connector_limit
        """

        if not encoding or not encoding.strip():
            raise ValueError("`encoding` must be a non-empty string!")

        if backoff_factor is not None and backoff_factor < 0:
            raise ValueError("`backoff_factor` must be non-negative!")

        if timeout <= 0:
            raise ValueError("`timeout` must be positive!")

        if timeout > 3600:
            raise ValueError("`timeout` should not exceed 3600 seconds!")

        if connector_limit <= 0:
            raise ValueError("`connector_limit` must be positive!")

        if connector_limit_per_host <= 0:
            raise ValueError("`connector_limit_per_host` must be positive!")

        if connector_limit_per_host > connector_limit:
            raise ValueError(
                "`connector_limit_per_host` cannot exceed `connector_limit`!"
            )

        self.backoff_factor = backoff_factor
        self.retries = retries

        self.encoding = encoding
        self.raise_for_status = raise_for_status
        self.timeout = timeout

        self.connector_limit = connector_limit
        self.connector_limit_per_host = connector_limit_per_host

    @classmethod
    def registration_key(cls) -> str:
        return cls.engine()

    @classmethod
    @abstractmethod
    def engine(cls) -> str:
        """
        Return the unique engine identifier for this requester implementation.

        This method must be implemented by all concrete requester classes to
        provide a unique string identifier for the HTTP library they use.
        The identifier is used by the factory pattern for requester registration
        and instantiation.

        Returns:
            str: Unique engine identifier (e.g., "aiohttp", "requests", "urllib3").
        """

    @abstractmethod
    def request(
        self,
        url: str,
        method: HTTPMethod,
        headers: Optional[Dict[str, str]] = None,
        retries: Optional[Any] = None,
        backoff_factor: Optional[float] = None,
        **kwargs,  # Each `engine`have its own attributes...
    ) -> Any:
        """
        Execute an HTTP request with the specified parameters.

        This abstract method must be implemented by all concrete requester classes
        to perform the actual HTTP request using their underlying library. The method
        should handle retry logic, error mapping, and return appropriate response objects.

        Args:
            url: The target URL for the HTTP request. Must be a valid HTTP/HTTPS URL.

            method: HTTP method to use for the request. Should be one of the standard
                HTTP methods (GET, POST, PUT, DELETE, etc.) from the HTTPMethod enum.

            headers: Optional HTTP headers to include in the request. These headers
                will be merged with any session-level or default headers configured
                in the requester.

            retries: Retry strategy for this specific request. Can override the
                instance-level retry configuration. The interpretation depends on
                the implementation:
                - None: Use instance default
                - False/0: Disable retries for this request
                - Integer: Number of retry attempts
                - Object: Library-specific retry configuration

            backoff_factor: Exponential backoff multiplier for retry delays.
                Can override the instance-level backoff configuration.
                Must be non-negative if provided.

            **kwargs: Additional implementation-specific parameters. Each concrete
                requester may accept different kwargs based on the underlying library:
                - aiohttp: timeout, params, json, data, cookies, ssl, etc.
                - requests: timeout, params, json, data, cookies, verify, etc.
                - urllib3: timeout, fields, body, preload_content, etc.

        Returns:
            Any: Response object specific to the underlying HTTP library:
                - aiohttp: ClientResponse
                - requests: Response
                - urllib3: HTTPResponse

        Raises:
            The method should use raise_custom_exception() to map HTTP status codes
            to appropriate exceptions:
                - AuthenticationException: For 401 Unauthorized
                - AuthorizationException: For 403 Forbidden
                - RateLimitException: For 429 Too Many Requests (when retries exhausted)
                - RetryableException: For 502/503/504 server errors (when retries exhausted)
                - ServiceException: For other 4xx client errors
                - InternalServerError: For 5xx server errors (when retries exhausted)

        Note:
            Implementations should respect the instance-level configuration
            (raise_for_status, timeout, etc.) while allowing per-request overrides
            through the kwargs parameter.
        """

    def _get_response_encoding(
        self,
        headers: Dict[str, str],
        default: str = "utf-8",
    ) -> str:
        """
        Determine the character encoding for response content from HTTP headers.

        This method performs automatic encoding detection by examining HTTP response
        headers in order of priority. It handles various charset declaration formats
        including quoted and unquoted values commonly found in real-world HTTP responses.

        Detection Order:
            1. Direct "charset" header (rare but takes highest priority)
            2. "charset=" parameter in Content-Type header (most common)
            3. Instance-level encoding setting
            4. Provided default parameter

        Args:
            headers: HTTP response headers as a case-insensitive dictionary.
                Common headers examined: "charset", "content-type".

            default: Fallback encoding to use when no charset information
                is found in headers or instance settings. Defaults to "utf-8".

        Returns:
            str: The detected or fallback character encoding name.
                Examples: "utf-8", "iso-8859-1", "windows-1252".

        Note:
            - Header names are compared case-insensitively
            - Charset values are stripped of surrounding whitespace
            - Both single and double quotes are removed from charset values
            - The method gracefully handles malformed or missing headers
        """

        headers_ = {
            k.lower(): v
            for k, v in headers.items()
        }

        # First trying "charset" header directly (rare)...
        charset = headers_.get("charset")
        if charset:
            return charset.strip()

        # Then checking `Content-Type` for "charset="
        content_type = headers_.get("content-type", "")
        match = re.search(r"charset=([^\s;]+)", content_type, re.IGNORECASE)
        if match:
            return (
                match.group(1)
                    .strip()
                    .replace("'", "")
                    .replace('"', "")
            )

        return self.encoding or default

    @staticmethod
    def raise_custom_exception(
        status_code: int,
        details: str,
        within_retry: bool = False,
    ):
        """
        Raise appropriate HTTP exception based on status code and retry context.

        This method implements standardized HTTP status code to exception mapping
        for all requester implementations. It provides intelligent handling of
        rate limiting scenarios based on whether the request is within a retry
        cycle or has exhausted all retry attempts.

        The method ensures consistent exception behavior across different HTTP
        libraries while maintaining proper retry semantics for recoverable errors.

        Args:
            status_code: HTTP status code from the failed response.
                Should be a standard HTTP status code (100-599).

            details: Descriptive error message providing context about the failure.
                Typically includes the response body or error description.

            within_retry: Whether this exception is being raised during active retry
                attempts. Affects the exception type for 429 (rate limit) responses:
                - False: Raises RateLimitException (no more retries)
                - True: Raises RetryableException (can be retried)

        Raises:
            AuthenticationException: For 401 Unauthorized responses.
                Indicates invalid or missing authentication credentials.

            AuthorizationException: For 403 Forbidden responses.
                Indicates insufficient permissions for the requested resource.

            RateLimitException: For 429 Too Many Requests when within_retry=False.
                Indicates rate limit exceeded and no retries remaining.

            RetryableException: For retryable errors (429, 502, 503, 504) when
                within_retry=True. Indicates the request can be retried.

            ServiceException: For other 4xx client errors (400, 404, 405, etc.).
                Indicates client-side request problems that shouldn't be retried.

            InternalServerError: For 5xx server errors and any unrecognized
                status codes. Default fallback for server-side problems.

        Note:
            The within_retry parameter only affects 429 status code handling.
            All other status codes map to the same exception types regardless
            of retry context.
        """

        error_cls = InternalServerError

        if status_code == 401:
            error_cls = AuthenticationException

        elif status_code == 403:
            error_cls = AuthorizationException

        elif status_code == 429 and not within_retry:
            # Only raise it if not retrying, otherwise must reach out
            # next condition.
            error_cls = RateLimitException

        elif status_code in (429, 502, 503, 504) and within_retry:
            error_cls = RetryableException

        elif 400 <= status_code < 500:
            error_cls = ServiceException

        raise error_cls(
            status_code=status_code,
            details=details,
        )
