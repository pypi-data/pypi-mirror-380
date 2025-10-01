import time
from multiprocessing import Process

import pytest
from killport import kill_ports
from psutil import NoSuchProcess

from lsrestclient import LsRestClient, LsRestClientBackendEnum


@pytest.fixture(scope="session")
def rest_client_pytest():
    return LsRestClient(
        base_url="http://localhost:9000",
        name="pytest",
        cache=True,
        cache_backend=LsRestClientBackendEnum.redis,
        stale_while_revalidate=True,
    )


@pytest.fixture(scope="session")
def app_server():
    try:
        kill_ports(ports=[9000])
    except NoSuchProcess:
        pass

    from test_app.main import run_server

    proc = Process(
        target=run_server, args=(), kwargs={"log_level": "warning"}, daemon=True
    )
    proc.start()
    retries = 5
    retry = 0
    while retry < retries:
        # noinspection PyBroadException
        try:
            client = LsRestClient("main_up", cache=False)
            r = client.get("/healthz")
            assert r.status_code == 200
            break
        except Exception:
            time.sleep(1)
            retry += 1
            continue
    yield
    proc.kill()
