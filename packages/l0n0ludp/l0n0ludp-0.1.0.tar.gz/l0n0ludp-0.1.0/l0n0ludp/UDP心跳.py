import asyncio
import time
from .UDP消息 import UDP消息, UDP消息类型
from typing import Tuple


class UDP心跳:
    def __init__(
            self,
            传输: asyncio.DatagramTransport,
            会话ID: int,
            心跳间隔: float = 2.0,
            地址: Tuple[str, int] | None = None) -> None:
        self.传输 = 传输
        self.会话ID = 会话ID
        self.心跳间隔 = 心跳间隔
        self.地址 = 地址
        self.心跳发送时间辍 = time.time()
        self.心跳接收时间辍 = time.time()
        self.消息 = UDP消息(UDP消息类型.心跳, 会话ID, 地址=地址)
        self.链接断开 = False

    def 刷新发送(self):
        self.心跳发送时间辍 = time.time()

    def 刷新接收(self):
        self.心跳接收时间辍 = time.time()

    async def __call__(self):
        while not self.传输.is_closing():
            当前时间 = time.time()
            if 当前时间 - self.心跳发送时间辍 > self.心跳间隔:
                self.消息.发送(self.传输, False)
                self.心跳发送时间辍 = 当前时间
            if 当前时间 - self.心跳接收时间辍 > self.心跳间隔 * 2:
                break
            await asyncio.sleep(1)
        self.链接断开 = True
