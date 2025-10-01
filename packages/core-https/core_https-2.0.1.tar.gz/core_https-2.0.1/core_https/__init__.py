# -*- coding: utf-8 -*-

from core_mixins import StrEnum

try:
    from http import HTTPStatus as _HTTPStatus

except ImportError:
    from .utils import HTTPStatus as _HTTPStatus  # type: ignore


__all__ = [
    "HTTPStatus",
    "StatusInfo"
]


# Type alias that works with both standard library
# and the custom HTTPStatus...
HTTPStatus = _HTTPStatus


class StatusInfo(StrEnum):
    """
    StatusInfo is a literal representation of the response depending on
    the status_code received...

      * success: is for HTTP statuses 1XX, 2XX and 3XX.
      * error: is for HTTP statuses from 400 to 499.
      * fail: is for HTTP statuses from 500 to 599.
    """

    SUCCESS = "success"
    ERROR = "error"
    FAILURE = "failure"
