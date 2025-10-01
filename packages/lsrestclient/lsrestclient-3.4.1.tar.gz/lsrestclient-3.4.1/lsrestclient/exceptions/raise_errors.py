import contextlib
import logging
from typing import List, Optional, Type

import pydash
from webexception.webexception import WebException

from lsrestclient.response import LsRestClientResponse

log = logging.getLogger(__name__)


@contextlib.contextmanager
def raise_errors(  # noqa: ANN201
    r: LsRestClientResponse, exceptions: Optional[List[Type[Exception]]] = None
):
    if exceptions is None:
        exceptions_by_class = {}
    else:
        exceptions_by_class = {e.__name__: e for e in exceptions}

    if r.status_code < 399:
        yield r
    else:
        try:
            json = r.json()
        except Exception:
            log.error(r.content)
            raise WebException(status_code=r.status_code, detail=r.content)

        detail = pydash.get(json, "detail", json)
        error_class = pydash.get(detail, "error_class", None)
        if error_class is not None:
            payload = pydash.get(detail, "error_payload", {})
        else:
            error_class = pydash.get(detail, "ERROR_CLASS", None)
            payload = {}

        if error_class in exceptions_by_class:
            # noinspection PyArgumentList
            e = exceptions_by_class[error_class](**payload)
            raise e
        # backend errors
        raise WebException(status_code=r.status_code, detail=detail)
