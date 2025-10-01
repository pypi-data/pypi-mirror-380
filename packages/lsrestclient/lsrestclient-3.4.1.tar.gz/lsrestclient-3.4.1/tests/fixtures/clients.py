import pytest

from lsrestclient import LsRestClient

LsRestClient(base_url="http://localhost:9000", name="echo", cache=False)
LsRestClient(base_url="http://localhost:9000", name="cached_echo", cache=True)


@pytest.fixture(scope="session")
def echo_client(app_server):
    return LsRestClient.client("echo")


@pytest.fixture(scope="session")
def cached_echo_client(app_server):
    return LsRestClient.client("cached_echo")
