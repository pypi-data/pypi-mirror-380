import random
from abc import ABC, abstractmethod
from datetime import datetime
from typing import Any

from loguru import logger
from typing_extensions import TypedDict

from ..adapters.web import WebRequester
from ..config import tz
from ..exceptions import ResponseCodeError


class Note(TypedDict):
    create_time: str | None
    source: str


class BaseWebAccount(ABC):
    """Web账号基类"""

    available: bool = True
    uid: int
    cookies: dict[str, Any]
    web_requester: WebRequester
    note: Note
    type: str = "Base"

    def __init__(
        self,
        uid: str | int,
        cookies: dict[str, Any],
        note: Note | None = None,
    ) -> None:
        self.uid = int(uid)
        self.note = note or {
            "create_time": datetime.now(tz=tz).isoformat(timespec="seconds"),
            "source": "",
        }
        self.cookies = cookies
        self.web_requester = WebRequester(cookies=self.cookies, update_callback=self.update)

    @property
    def info(self) -> dict[str, Any]:
        """导出账号信息"""
        return {
            "uid": self.uid,
            "type": self.type,
            "note": self.note,
        }

    @property
    def info_str(self) -> str:
        """导出账号信息"""
        return f"[{self.type}] UID: <{self.uid}> Note: {self.note}"

    async def check_alive(self) -> bool:
        """检查账号是否存活"""
        try:
            logger.debug(f"查询 Web 账号 <{self.uid}> 存活状态")
            await self.web_requester.check_new_dynamics(0)
            logger.debug(f"Web 账号 <{self.uid}> 确认存活")
            self.available = True
        except ResponseCodeError as e:
            if e.code != -101:
                raise
            logger.error(f"Web 账号 <{self.uid}> 已失效: {e}")
            self.available = False
        except Exception as e:
            logger.error(f"Web 账号 <{self.uid}> 检查存活状态时发生异常: {e}")
            self.available = False
        return self.available

    def update(self, cookies: dict[str, Any]) -> bool:
        """更新cookies"""
        old_cookies = self.cookies
        self.cookies.update(cookies)
        if old_cookies == self.cookies:
            return False
        self._on_cookies_updated()
        return True

    @abstractmethod
    def _get_dump_cookies(self) -> dict[str, Any]:
        """获取用于导出的cookies信息"""

    @abstractmethod
    def _on_cookies_updated(self) -> None:
        """cookies更新后的处理"""


class TemporaryWebAccount(BaseWebAccount):
    """临时账号"""

    type: str = "Temporary"

    def __init__(self) -> None:
        super().__init__(random.randint(1, 100), {})
        self.available = True

    def _get_dump_cookies(self) -> dict[str, Any]:
        return {}

    def _on_cookies_updated(self) -> None:
        pass


class RecoverableWebAccount(BaseWebAccount, ABC):
    """可恢复账号"""

    type: str = "Recoverable"

    @abstractmethod
    async def recover(self) -> bool:
        """尝试恢复账号, 返回是否成功"""
