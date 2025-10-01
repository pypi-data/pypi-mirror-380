#!/usr/bin/python
# -*- coding: utf-8 -*-
import logging

logging.getLogger("urllib3").setLevel(logging.WARNING)
logging.getLogger("requests_cache").setLevel(logging.WARNING)
# logging.getLogger("requests_cache").setLevel(logging.DEBUG)

pytest_plugins = ["tests.fixtures.app_server", "tests.fixtures.clients"]
# pytest_plugins = ["tests.fixtures.docker_compose"]
