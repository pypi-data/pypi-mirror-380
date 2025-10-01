# -*- coding: utf-8 -*-

import json
from contextlib import suppress
from typing import Dict, Optional

from urllib3 import BaseHTTPResponse
from urllib3 import PoolManager
from urllib3 import Retry

from .base import HTTPMethod
from .base import IRequester


class Urllib3Requester(IRequester):
    """
    It uses `urllib3` to make the requests.

    .. code-block:: python

        from core_https.requesters.urllib3_ import Urllib3Requester
        from core_https.utils import HTTPMethod

        requester: Urllib3Requester = IRequester.get_class(Urllib3Requester.engine())()
        response = requester.request(method=HTTPMethod.GET, url="https://google.com")
        print(response.data.decode())
    ..
    """

    def __init__(
        self,
        pool_manager: Optional[PoolManager] = None,
        retries: Optional[Retry] = None,
        **kwargs,
    ) -> None:
        """
        :param pool_manager: The pool manager to use or one will be created.
        :param retries: Retry strategy to apply. Pass zero (0) to avoid retries.
        """

        super().__init__(**kwargs)

        if not pool_manager:
            pool_manager = PoolManager()

        self._http: PoolManager = pool_manager
        self.retries = retries

    @classmethod
    def engine(cls):
        return "urllib3"

    def request(
        self,
        url: str,
        method: HTTPMethod = HTTPMethod.GET,
        headers: Optional[Dict[str, str]] = None,
        retries: Optional[Retry] = None,
        backoff_factor: Optional[float] = None,
        fields: Optional[Dict] = None,
        timeout: Optional[float] = None,
        **kwargs,
    ) -> BaseHTTPResponse:
        """
        :raises: `ServiceException` for other 4XX status_code.
        :raises: `AuthenticationException` for status_code == 401.
        :raises: `AuthorizationException` for status_code == 403.
        :raises: `InternalServerError` for status_code >= 500.

        :returns: `HTTPResponse` object.
        """

        backoff_factor = (
            backoff_factor
            if backoff_factor is not None
            else self.backoff_factor
            if self.backoff_factor is not None
            else 0.5
        )

        retries_ = retries or self.retries
        if retries_ is None:
            retries_ = Retry(
                status_forcelist=[429, 502, 503, 504],
                backoff_factor=backoff_factor,
                total=3,
            )

        response = self._http.request(
            method=str(method),
            url=url,
            headers=headers,
            fields=fields,
            timeout=timeout or self.timeout,
            retries=retries_,
            **kwargs,
        )

        status_code = response.status

        if status_code >= 400 and self.raise_for_status:
            info = response.data.decode(self._get_response_encoding(response.headers))  # type: ignore[arg-type]
            headers_ = {k.lower(): v for k, v in response.headers.items()}

            if "application/json" in headers_.get("content-type", ""):
                if hasattr(response, "json"):
                    info = response.json()

                else:
                    with suppress(json.JSONDecodeError):
                        info = json.loads(info)

            self.raise_custom_exception(status_code, info)

        return response
