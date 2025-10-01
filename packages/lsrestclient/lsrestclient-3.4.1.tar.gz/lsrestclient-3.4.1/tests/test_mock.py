from lsrestclient import LsRestClient, LsRestClientResponse
from lsrestclient.mock import lsrestclient_mock_context

LsRestClient(
    base_url="http://localhost:9000",
    name="echo",
)


def test_basic_mock():
    client = LsRestClient.client("echo")

    with lsrestclient_mock_context() as mocker:
        test_mock = mocker.mock(
            client,
            "GET",
            "/test",
            return_value=LsRestClientResponse.from_dict(200, {"a": "test"}),
        )
        other_mock = mocker.mock(
            client,
            "GET",
            "/other",
            return_value=LsRestClientResponse.from_dict(402, {"a": "other"}),
        )

        client.get("/test")  # mocked
        client.get("/test")  # mocked
        client.patch("/test")  # not_mocked
        client.get("/other")  # mocked
        client.delete("/other")  # not_mocked

        assert test_mock.call_count == 2
        assert other_mock.call_count == 1

    client.get("/test")  # not mocked anymore
    assert test_mock.call_count == 2  # still two (hopefully)


def test_fixture_mock(lsrestclient_mocker):
    client = LsRestClient.client("echo")
    test_mock = lsrestclient_mocker.mock(
        client,
        "GET",
        "/test",
        return_value=LsRestClientResponse.from_dict(200, {"a": "test"}),
    )

    client.get("/test")  # not mocked anymore

    assert test_mock.call_count == 1  # still two (hopefully)


def test_fixture_unmock_single(lsrestclient_mocker, app_server):
    client = LsRestClient.client("echo")
    test_mock = lsrestclient_mocker.mock(
        client,
        "GET",
        "/test",
        return_value=LsRestClientResponse.from_dict(200, {"a": "test"}),
    )
    test_mock_2 = lsrestclient_mocker.mock(
        client,
        "PATCH",
        "/test",
        return_value=LsRestClientResponse.from_dict(200, {"a": "test"}),
    )
    assert len(lsrestclient_mocker.mocks) == 2

    client.get("/test")
    client.patch("/test")
    assert test_mock.call_count == 1  # still two (hopefully)

    lsrestclient_mocker.unmock(client, "PATCH", "/test")

    assert len(lsrestclient_mocker.mocks) == 1
    client.patch("/test")

    test_mock.reset_mock()
    test_mock_2.reset_mock()
