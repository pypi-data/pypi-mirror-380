import asyncio
import re
from base64 import b64encode
from typing import Literal

from fastapi import APIRouter
from pydantic import BaseModel

from bilichat_request.account import get_web_account
from bilichat_request.config import config
from bilichat_request.exceptions import NotFindAbortError
from bilichat_request.functions import dynamic_content
from bilichat_request.functions.render import column, dynamic
from bilichat_request.functions.render.video import style_blue
from bilichat_request.functions.tools import bv2av

from .base import error_handler

router = APIRouter()


class Content(BaseModel):
    type: Literal["video", "column", "dynamic"]
    id: str
    b23: str
    img: str

    @classmethod
    async def video(cls, video_id: int | str, quality: int = 75) -> "Content":
        img, info = await asyncio.wait_for(style_blue.screenshot(video_id, quality=quality), timeout=config.timeout)
        return cls(type="video", id=info.aid, b23=info.b23_url, img=b64encode(img).decode())

    @classmethod
    async def column(cls, cvid: int | str, quality: int = 75) -> "Content":
        cvid = str(cvid)
        if cvid.startswith("cv"):
            cvid = cvid[2:]
        async with get_web_account() as account:
            b23 = await account.web_requester.get_b23_url(f"cv{cvid}")
        img = await asyncio.wait_for(column.screenshot(cvid=cvid, quality=quality), timeout=config.timeout)
        return cls(type="column", id=f"cv{cvid}", b23=b23, img=b64encode(img).decode())

    @classmethod
    async def dynamic(cls, dynamic_id: str, quality: int = 75, *, mobile_style: bool = True) -> "Content":
        async with get_web_account() as account:
            b23 = await account.web_requester.get_b23_url(f"https://t.bilibili.com/{dynamic_id}")
        img = await asyncio.wait_for(
            dynamic.screenshot(dynamic_id, mobile_style=mobile_style, quality=quality), timeout=config.timeout
        )
        return cls(type="dynamic", id=dynamic_id, b23=b23, img=b64encode(img).decode())


class DynamicContentResponse(BaseModel):
    """动态内容响应模型"""
    text: str  # 文字内容，无内容时为 ""
    images: list[str]  # 图片链接列表，无内容时为 []


@router.get("/video")
@error_handler
async def get_video(video_id: int | str, quality: int = 75) -> Content:
    return await Content.video(video_id, quality=quality)


@router.get("/column")
@error_handler
async def get_column(cvid: int | str, quality: int = 75) -> Content:
    return await Content.column(cvid, quality=quality)


@router.get("/dynamic")
@error_handler
async def get_dynamic(dynamic_id: str, quality: int = 70, *, mobile_style: bool = False) -> Content:
    return await Content.dynamic(dynamic_id, quality=quality, mobile_style=mobile_style)


@router.get("/dynamic_content")
@error_handler
async def get_dynamic_content(dynamic_id: str) -> DynamicContentResponse:
    """
    获取动态的文字内容和图片链接
    
    Args:
        dynamic_id: 动态ID
        
    Returns:
        DynamicContentResponse: 包含文字内容和图片链接的对象
            - text: str - 文字内容, 无内容时为 ""
            - images: list[str] - 图片链接列表, 无内容时为 []
    """
    result = await dynamic_content.extract_dynamic_content(dynamic_id)
    return DynamicContentResponse(text=result.text, images=result.images)


@router.get("/")
@error_handler
async def get_content(bililink: str) -> Content:
    if matched := re.search(r"(?i)av(\d{1,15})|bv(1[0-9a-z]{9})", bililink):
        _id = str(matched.group()).removeprefix("av").removeprefix("AV")
        _id = int(_id) if _id.isdigit() else bv2av(_id)
        return Content(type="video", id=f"av{_id}", b23="", img="")

    elif matched := re.search(r"cv(\d{1,16})", bililink):
        _id = matched.group()
        return Content(type="column", id=_id, b23="", img="")

    elif matched := re.search(r"(dynamic|opus|t.bilibili.com)/(\d{1,128})", bililink):
        _id = matched.groups()[-1]
        return Content(type="dynamic", id=_id, b23="", img="")
    else:
        raise NotFindAbortError(f"无法解析的链接 {bililink}")
