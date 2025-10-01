import asyncio
import datetime
import time
from contextlib import contextmanager

from fastapi_lsoft import next_midnight


@contextmanager
def measure_time():
    d = {
        "start": time.time(),
        "end": None,
        "elapsed": None,
    }
    yield d
    d["end"] = time.time()
    d["elapsed"] = d["end"] - d["start"]


def test_cache(app_server, rest_client_pytest):
    rest_client_pytest.clear_cache()
    for i in range(10):
        r = rest_client_pytest.get("/tax_rates")
        assert r.status_code == 200
        assert r.from_cache == (i != 0)  # the first round is not cached


def test_cache_without_cache_control(app_server, rest_client_pytest):
    rest_client_pytest.clear_cache()
    for i in range(10):
        r = rest_client_pytest.get("/stock")
        assert r.status_code == 200
        assert r.from_cache is False


def test_cache_with_expire_after(app_server, rest_client_pytest):
    rest_client_pytest.clear_cache()
    midnight = next_midnight(datetime.UTC)
    r = rest_client_pytest.get("/tax_rates", expire_after=midnight)
    assert r.from_cache is False
    r = rest_client_pytest.get("/tax_rates", expire_after=midnight)
    assert r.from_cache is True


async def test_cache_etag(app_server, rest_client_pytest):
    rest_client_pytest.clear_cache()
    start = time.time()
    for i in range(30):
        diff = time.time() - start
        with measure_time() as t:
            r = rest_client_pytest.get("/product")
        print(
            f"{int(diff * 10) / 10:5.1f}s",
            f"{int(t['elapsed'] * 1000):3d}ms",
            r.status_code,
            r.headers.get("etag"),
            int(r.from_cache),
            r.json(),
            r.headers.get("cache-control", ""),
        )
        await asyncio.sleep(1)

    # r = rest_client_pytest.get("/product")
    # assert r.from_cache == True
