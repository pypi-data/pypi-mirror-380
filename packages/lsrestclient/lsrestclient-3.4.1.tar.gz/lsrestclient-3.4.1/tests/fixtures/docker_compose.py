import os
import subprocess

import pytest


@pytest.fixture(scope="session", autouse=True)
def docker_compose_up():
    fpath = os.path.abspath(
        os.path.join(os.path.dirname(__file__), "..", "..", "docker-compose.yml")
    )
    for container in ["echo"]:
        print(f"starting {fpath} {container}")
        subprocess.call(
            ["docker", "compose", "-f", fpath, "-p", "pytest", "up", "-d", container]
        )
