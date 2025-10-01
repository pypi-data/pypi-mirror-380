import logging
from abc import ABC, abstractmethod
from typing import Any

from lsrestclient import LsRestClient, LsRestClientResponse

log = logging.getLogger(__name__)


class LsFastApiClientBase(ABC):
    _client = None
    client_name = None

    def __init__(self) -> None:
        pass

    @classmethod
    def client(cls) -> LsRestClient:
        # noinspection PyBroadException
        try:
            cls._client = LsRestClient.client(cls.client_name)
        except Exception:  # pragma: no cover
            # noinspection PyArgumentList
            cls._client = cls.register()
        return cls._client

    @classmethod
    def register(cls, base_url: str | None = None, **kwargs: Any) -> LsRestClient:
        # noinspection PyArgumentList
        log.debug(f"Registering {cls.client_name} API client at {base_url}")
        cls._client = LsRestClient(
            name=cls.client_name, base_url=base_url or cls.base_url(), **kwargs
        )
        return cls._client

    @classmethod
    def health(cls) -> LsRestClientResponse:
        return cls.client().get("/healthz")

    @classmethod
    @abstractmethod
    def base_url(cls) -> str:
        raise NotImplementedError
