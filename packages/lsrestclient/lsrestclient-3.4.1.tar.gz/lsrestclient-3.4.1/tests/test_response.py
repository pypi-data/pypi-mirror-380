from lsrestclient import LsRestClientResponse


def test_from_dict():
    # noinspection PyTypeChecker
    res = LsRestClientResponse.from_dict(
        status_code=200, data={"a": "b"}, headers={"nix": "0"}
    )
    print("res", res)

    json = res.json()
    print("json", json)
    assert json is not None


def test_from_dict_empty():
    # noinspection PyTypeChecker
    res = LsRestClientResponse(status_code=200, content="", headers={})
    print("res", res)
    json = res.json()
    print("json", json)
    assert json is None
