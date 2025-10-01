import asyncio
import hashlib
import logging
import time
from contextlib import asynccontextmanager

import uvicorn
from fastapi import Depends, FastAPI
from fastapi_lsoft.depends import CacheControlDepends, EtagDepends
from fastapi_lsoft.middleware import FastapiLsoftMiddleware
from starlette.requests import Request

log = logging.getLogger(__name__)

# setup 3rd party loggers
logging.getLogger("asyncio").setLevel(logging.WARNING)


# noinspection PyShadowingNames
@asynccontextmanager
async def lifespan(app: FastAPI):  # noqa: ANN201
    assert app
    # Initializations
    yield  # execute Application
    # Cleanups


app = FastAPI(lifespan=lifespan)
app.add_middleware(FastapiLsoftMiddleware)


@app.get("/")
async def root() -> dict:
    return {"message": "Hello World"}


@app.get("/healthz")
async def router_healthz_get() -> dict:
    return {"health": "healthy"}


@app.get("/echo")
async def router_echo_get(request: Request) -> dict:
    return {"request": {"headers": dict(request.headers)}}


@app.get("/tax_rates", dependencies=[Depends(CacheControlDepends(max_age=30))])
async def rooter_tax_rates_get() -> dict:
    # await asyncio.sleep(0.1)
    return {"LU": {"STANDARD": 17.0}}


@app.get("/stock")
async def router_stock_get() -> dict:
    # await asyncio.sleep(1)
    return {"137097": 10}


async def router_product_get_etag(json_body: dict) -> str:
    ret = hashlib.md5(str(tuple(sorted(json_body.items()))).encode("utf-8")).hexdigest()
    return ret


@app.get(
    "/product",
    dependencies=[
        Depends(EtagDepends(etag_generator=router_product_get_etag)),
        Depends(CacheControlDepends(max_age=5)),
    ],
)
async def router_product_get() -> dict:
    print("endpoint called")
    await asyncio.sleep(0.5)
    t = int(time.time() / 10) % 10
    d = {"sku": 137097, "stock": 10 + t}
    return d


def run_server(
    reload: bool = False, log_level: str = "info"
) -> None:  # pragma: no cover
    uvicorn.run(
        "test_app.main:app",
        host="0.0.0.0",
        port=9000,
        log_level=log_level,
        reload=reload,
    )


if __name__ == "__main__":  # pragma: no cover
    run_server(reload=True, log_level="info")
