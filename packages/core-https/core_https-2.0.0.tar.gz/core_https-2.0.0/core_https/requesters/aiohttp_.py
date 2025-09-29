# -*- coding: utf-8 -*-

from __future__ import annotations

import asyncio
from typing import Any
from typing import Dict
from typing import Optional

try:
    from typing import Self

except ImportError:
    from typing_extensions import Self

from aiohttp import (
    ClientResponse,
    ClientResponseError,
    ClientSession,
    ClientTimeout,
    TCPConnector,
)

from .base import IRequester
from .base import HTTPMethod


class AioHttpRequester(IRequester):
    """
    Asynchronous HTTP requester implementation using aiohttp.

    This class provides an async HTTP client interface using the aiohttp library.
    It supports automatic session management, configurable retry logic with exponential
    backoff, connection pooling, and comprehensive error handling.

    The requester can work with externally provided ClientSession objects or create
    and manage its own session internally. It implements the async context manager
    protocol for convenient resource cleanup.

    Features:
        - Automatic session creation and management
        - Configurable retry logic with exponential backoff
        - Connection pooling with configurable limits
        - Comprehensive HTTP exception mapping
        - Support for custom timeouts per request
        - Context manager support for resource cleanup

    .. code-block:: python

        import aiohttp
        from core_https.requesters.aiohttp_ import AioHttpRequester
        from core_https.utils import HTTPMethod

        requester: AioHttpRequester = AioHttpRequester(raise_for_status=True)

        async def get():
            # This is optional as the client creates one session for you if not provided.
            session = aiohttp.ClientSession()

            try:
                response = await requester.request(
                    method=HTTPMethod.GET,
                    session=session,
                    url=url,
                    params={
                        "x-api-key": "..."
                    })

                return await response.text()

            except Exception as error:
                pass

            finally:
                await session.close()

        res = asyncio.run(get())
        print(res)
    ..
    """

    def __init__(
        self,
        session: Optional[ClientSession] = None,
        retries: Optional[int] = 3,
        **kwargs,
    ) -> None:
        """
        Initialize the AioHttpRequester.

        Args:
            session: Optional pre-configured aiohttp ClientSession to use for requests.
                If not provided, a new session will be created automatically with
                the configured timeout and connection limits. When providing a custom
                session, you are responsible for closing it.

            retries: Number of retry attempts for failed requests. Defaults to 3.
                Set to 0 to disable retries completely. Only applies to retryable
                errors like network timeouts and server errors (5xx status codes).

            **kwargs: Additional arguments passed to the base IRequester class,
                including encoding, raise_for_status, backoff_factor, timeout,
                connector_limit, and connector_limit_per_host.

        Note:
            The timeout specified in kwargs becomes the default session timeout.
            Individual requests can override this using the timeout parameter
            in the request() method.
        """

        super().__init__(**kwargs)

        self._session = session
        self._session_lock = asyncio.Lock()
        self._owns_session = session is None
        self._timeout = ClientTimeout(total=self.timeout)
        self.retries = retries

    async def __aenter__(self) -> Self:
        await self._ensure_session()
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb) -> None:
        await self.close()

    @classmethod
    def engine(cls) -> str:
        return "aiohttp"

    async def _ensure_session(self) -> ClientSession:
        """
        Ensure a ClientSession exists, creating one if necessary.

        This method implements a thread-safe lazy initialization pattern using
        double-checked locking to ensure only one session is created even when
        called concurrently from multiple coroutines.

        Returns:
            ClientSession: The active aiohttp ClientSession instance.

        Note:
            If a session was provided in the constructor, it will be returned as-is.
            If no session was provided, a new one will be created with the configured
            timeout and connection limits.

        Thread Safety:
            This method is safe to call concurrently from multiple coroutines.
            The double-check locking pattern ensures only one session is created.
        """

        if self._session is None:
            async with self._session_lock:
                if self._session is None:  # Double-check after acquiring lock...
                    self._session = ClientSession(
                        timeout=self._timeout,
                        connector=TCPConnector(
                            limit=self.connector_limit,
                            limit_per_host=self.connector_limit_per_host,
                        ),
                    )

                    self._owns_session = True

        return self._session

    async def request(
        self,
        url: str,
        method: HTTPMethod = HTTPMethod.GET,
        headers: Optional[Dict[str, Any]] = None,
        retries: Optional[int] = None,
        backoff_factor: Optional[float] = None,
        session: Optional[ClientSession] = None,
        params: Optional[Dict[str, Any]] = None,
        timeout: Optional[float] = None,
        **kwargs,
    ) -> ClientResponse:
        """
        Make an asynchronous HTTP request with retry logic.

        This method performs HTTP requests with automatic retry functionality,
        exponential backoff, and comprehensive error handling. Failed requests
        are retried based on the configured retry policy.

        Args:
            url: The target URL for the HTTP request.

            method: HTTP method to use. Defaults to GET. Supports all standard
                HTTP methods (GET, POST, PUT, DELETE, etc.).

            headers: Optional HTTP headers to include in the request. These will
                be merged with any session-level headers.

            retries: Number of retry attempts for this specific request.
                If not provided, uses the instance-level retry setting.
                Set to 0 to disable retries for this request.

            backoff_factor: Multiplier for exponential backoff between retries.
                The actual delay is calculated as: backoff_factor * attempt_number.
                If not provided, uses the instance-level setting or defaults to 0.5.

            session: Optional ClientSession to use for this request.
                If not provided, uses the requester's session (creating one if necessary).
                Useful for per-request session customization.

            params: URL query parameters to include in the request.
                Will be properly URL-encoded and appended to the URL.

            timeout: Request timeout in seconds for this specific request.
                Overrides the instance-level timeout setting.
                Set to None to use the default timeout.

            **kwargs: Additional parameters passed to aiohttp's request method.
                Common options include: json, data, cookies, ssl, proxy, etc.
                See aiohttp.ClientSession.request documentation for full list.

        Returns:
            ClientResponse: The aiohttp response object. Use methods like
                .json(), .text(), .read() to extract the response content.

        Raises:
            AuthenticationException: For 401 Unauthorized responses.
            AuthorizationException: For 403 Forbidden responses.
            RateLimitException: For 429 Too Many Requests (when retries exhausted).
            RetryableException: For 502/503/504 server errors (when retries exhausted).
            ServiceException: For other 4xx client errors.
            InternalServerError: For 5xx server errors (when retries exhausted).

        Note:
            The retry logic only applies to network errors and server errors (5xx).
            Client errors (4xx) are not retried, except for 429 (rate limit)
            which may be retried based on the configured policy.
        """

        session_ = session or await self._ensure_session()
        kwargs_ = kwargs.copy()

        if timeout is not None:
            kwargs_["timeout"] = ClientTimeout(total=timeout)

        retries = retries if retries is not None else self.retries
        if retries is None:
            retries = 3

        backoff_factor = (
            backoff_factor
            if backoff_factor is not None
            else self.backoff_factor
            if self.backoff_factor is not None
            else 0.5
        )

        attempts = 0

        while True:
            attempts += 1

            try:
                response = await session_.request(
                    method=str(method),
                    url=url,
                    headers=headers,
                    params=params,
                    **kwargs_,
                )

                if self.raise_for_status:
                    response.raise_for_status()

                return response

            except ClientResponseError as error:
                if attempts > retries:
                    self.raise_custom_exception(error.status, error.message)

                await asyncio.sleep(backoff_factor * attempts)

    async def close(self) -> None:
        """
        Close the internal session if it was created by this requester.

        This method performs cleanup of the internal ClientSession, but only
        if the session was created internally. If a custom session was provided
        in the constructor, it will not be closed as the caller is responsible
        for managing its lifecycle.

        The session reference is always cleared after calling this method,
        regardless of whether it was closed or not.

        Note:
            This method is automatically called when using the async context
            manager protocol (__aexit__). Manual calling is only necessary
            when not using the context manager pattern.
        """

        if self._session and self._owns_session:
            await self._session.close()
        self._session = None
