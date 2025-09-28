import asyncio
import itertools
from collections.abc import Callable
from contextlib import asynccontextmanager
from functools import wraps

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from loguru import logger
from sentry_sdk import capture_exception
from slowapi import Limiter
from slowapi.util import get_remote_address

from bilichat_request.adapters.browser import check_browser_health
from bilichat_request.compat import scheduler
from bilichat_request.config import NONEBOT_ENV
from bilichat_request.exceptions import AbortError, CaptchaAbortError, NotFindAbortError, ResponseCodeError
from bilichat_request.functions.tools import shorten_long_items

# 浏览器健康检查
if NONEBOT_ENV:
    from nonebot import get_driver  # type: ignore

    get_driver().on_startup(check_browser_health)

    app = FastAPI()
else:

    @asynccontextmanager
    async def lifespan(_: FastAPI):
        await check_browser_health()

        scheduler.start()
        yield

    app = FastAPI(lifespan=lifespan)

# 初始化 Limiter, 默认使用内存存储
limiter = Limiter(key_func=get_remote_address)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

_seqid_generator = itertools.count(0)


def error_handler(func: Callable):
    @wraps(func)
    async def wrapper(*args, **kwargs):  # noqa: ANN202
        try:
            seqid = f"{next(_seqid_generator)%1000000:6}"
            logger.bind(handler="request").trace(
                f"[{seqid}] ==> {func.__module__}.{func.__name__} {args if args else ''} {shorten_long_items(kwargs) if kwargs else ''}"
            )
            result = await func(*args, **kwargs)
            logger.bind(handler="request").trace(f"[{seqid}] <== {shorten_long_items(result)}")
        except asyncio.TimeoutError as e:
            logger.bind(handler="request").info(e)
            raise HTTPException(status_code=429, detail={"type": str(type(e)), "detail": str(e)}) from e
        except NotFindAbortError as e:
            logger.bind(handler="request").info(e)
            raise HTTPException(status_code=404, detail={"type": str(type(e)), "detail": str(e)}) from e
        except HTTPException as e:
            logger.bind(handler="request").info(f"{type(e)} {e.status_code} {e.detail}")
            raise
        except (AbortError, ResponseCodeError, CaptchaAbortError) as e:
            logger.bind(handler="request").error(e)
            logger.error(e)
            raise HTTPException(status_code=511, detail={"type": str(type(e)), "detail": str(e)}) from e
        except Exception as e:
            logger.bind(handler="request").exception(e)
            logger.exception(e)
            capture_exception(e)
            raise HTTPException(status_code=500, detail={"type": str(type(e)), "detail": str(e)}) from e
        return result

    return wrapper
