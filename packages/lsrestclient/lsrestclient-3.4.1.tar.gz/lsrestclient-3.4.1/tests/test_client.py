import os

import pytest as pytest

from lsrestclient import LsRestClient
from lsrestclient.contexts.bearer_token import bearer_token_provider


def test_from_env():
    os.environ["PUBLICAPIS_BASEURL"] = "https://api.publicapis.org"
    LsRestClient.from_env(
        "PUBLICAPIS_BASEURL",
        "publicapis",
    )


@pytest.mark.parametrize(
    "base_url, url, params, exp",
    [
        (
            "http://gammel.host:3000",
            "/gammel",
            None,
            "http://gammel.host:3000/gammel",
        ),
        (
            "http://gammel.local",
            "/test/me/right/here?with=some&query=parameters",
            None,
            "http://gammel.local/test/me/right/here?with=some&query=parameters",
        ),
        (
            "http://gammel.host:3000",
            "/gammel/{sku}/blah",
            {"sku": 137097},
            "http://gammel.host:3000/gammel/137097/blah",
        ),
    ],
)
def test_full_url(base_url, url, params, exp):
    full_url = LsRestClient(base_url=base_url).full_url(url, params)
    assert full_url == exp


def test_get(app_server):
    LsRestClient(
        base_url="http://localhost:9000",
        name="publicapis",
    )

    client = LsRestClient.client("publicapis")

    r = client.get("/")
    assert r.status_code == 200


def test_bearer_token(cached_echo_client):
    bt = "myverysecrettoken"
    with bearer_token_provider(bt):
        r = cached_echo_client.get("/echo", force_refresh=True)
        json = r.json()
        headers = json.get("request").get("headers", None)
        auth = headers.get("authorization", None)
        assert auth.startswith("Bearer")

    r = cached_echo_client.get("/echo", force_refresh=True)
    json = r.json()
    headers = json.get("request").get("headers", None)
    auth = headers.get("authorization", None)
    assert auth is None


def test_ignore_bearer_token(echo_client):
    bt = "myverysecrettoken1"
    bt2 = "myverysecrettoken2"

    with bearer_token_provider(bt):
        LsRestClient(
            base_url="http://localhost:9000",
            name="echo-2",
            ignore_bearer_context=True,
            cache=False,
        )
    with bearer_token_provider(bt2):
        echo2_client = LsRestClient.client("echo-2")
        r = echo2_client.get("/echo")
        json = r.json()
    auth = json.get("request").get("headers", None).get("authorization", None)
    assert auth == f"Bearer {bt}"

    with bearer_token_provider(bt):
        LsRestClient(
            base_url="http://localhost:9000",
            name="echo-3",
            ignore_bearer_context=False,
            cache=False,
        )
    with bearer_token_provider(bt2):
        echo3_client = LsRestClient.client("echo-3")
        r = echo3_client.get("/echo")
        json = r.json()
    auth = json.get("request").get("headers", None).get("authorization", None)
    assert auth == f"Bearer {bt2}"


def test_headers(echo_client):
    bt = "secrettoken"
    LsRestClient(
        base_url="http://localhost:9000",
        name="echo-4",
        ignore_bearer_context=True,
        headers={"x-foo": "bar"},
        cache=False,
    )
    LsRestClient(
        base_url="http://localhost:9000",
        name="echo-5",
        ignore_bearer_context=True,
        headers={},
        cache=False,
    )
    echo4_client = LsRestClient.client("echo-4")
    echo5_client = LsRestClient.client("echo-5")
    with bearer_token_provider(bt):
        r = echo4_client.get("/echo")
        json = r.json()
    x_foo = json.get("request").get("headers", None).get("x-foo", None)
    assert x_foo == "bar"

    with bearer_token_provider(bt):
        r = echo5_client.get("/echo")
        json = r.json()
    x_foo = json.get("request").get("headers", None).get("x-foo", None)
    assert x_foo is None
