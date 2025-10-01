from typing import Any, Generator

from lsrestclient.mock import LsRestClientMocker, lsrestclient_mock_context

try:
    import pytest

    @pytest.fixture
    def lsrestclient_mocker() -> Generator[LsRestClientMocker, Any, None]:
        with lsrestclient_mock_context() as mocker:
            yield mocker

except ImportError:
    pass
