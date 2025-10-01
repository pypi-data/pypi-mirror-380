# -*- coding: utf-8 -*-

from typing import Dict, Optional

import requests
import urllib3
from requests.adapters import HTTPAdapter

from core_https.requesters.base import IRequester
from .base import HTTPMethod


class RequestsRequester(IRequester):
    """
    It uses `requests` to make the requests.

    .. code-block:: python

        from core_https.requesters.requests_ import RequestsRequester
        from core_https.utils import HTTPMethod

        requester: RequestsRequester = RequestsRequester()

        response = requester.request(
            method=HTTPMethod.GET,
            url=url,
            params={
                "x-api-key": "..."
            })

        print(response.json())
    ..
    """

    def __init__(
        self,
        session: Optional[requests.Session] = None,
        retries: Optional[urllib3.Retry] = None,
        backoff_factor: Optional[float] = None,
        **kwargs,
    ) -> None:
        """
        :param session: Session to use for the requests.
        :param retries: Retry strategy to apply. Pass zero (0) to avoid retries.
        """

        super().__init__(**kwargs)
        self.retries = retries

        backoff_factor = (
            backoff_factor
            if backoff_factor is not None
            else self.backoff_factor
            if self.backoff_factor is not None
            else 0.5
        )

        if self.retries is None:
            self.retries = urllib3.Retry(
                status_forcelist=[429, 502, 503, 504],
                backoff_factor=backoff_factor,
                total=3,
            )

        adapter = HTTPAdapter(
            pool_connections=self.connector_limit,
            pool_maxsize=self.connector_limit_per_host,
            max_retries=self.retries,
        )

        if session is None:
            session = requests.Session()
            session.mount("https://", adapter)
            session.mount("http://", adapter)

        self._session = session

    @classmethod
    def engine(cls) -> str:
        return "requests"

    def request(  # type: ignore[override]
        self,
        url: str,
        method: HTTPMethod = HTTPMethod.GET,
        headers: Optional[Dict[str, str]] = None,
        retries: Optional[urllib3.Retry] = None,
        backoff_factor: Optional[float] = None,
        session: Optional[requests.Session] = None,
        params: Optional[Dict] = None,
        timeout: Optional[float] = None,
        **kwargs,
    ) -> requests.Response:
        """
        It makes the request using the session (externally provided or created
        if required) and return the response...

        :returns: `requests.Response` object.
        """

        session_ = session or self._session
        if params is None:
            params = {}

        response = session_.request(
            method=str(method.value),
            url=url,
            headers=headers,
            params=params,
            timeout=timeout,
            **kwargs,
        )

        try:
            if self.raise_for_status:
                response.raise_for_status()

        except requests.exceptions.HTTPError:
            status_code, info = response.status_code, response.text
            self.raise_custom_exception(status_code, info)

        return response
