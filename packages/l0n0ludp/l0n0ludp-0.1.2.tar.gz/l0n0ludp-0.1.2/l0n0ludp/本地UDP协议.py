import asyncio
import time
from .UDP消息 import UDP消息, UDP消息类型
from .UDP心跳 import UDP心跳
from .ChaCha20 import ChaCha20
from typing import Tuple


class 本地UDP客户端协议(asyncio.DatagramProtocol):
    def __init__(
            self,
            消息重传时间: float,
            消息重传最大次数: int,
            writer: asyncio.StreamWriter,
            心跳间隔: float,
            会话ID: int,
            密码: str):
        self.消息重传时间 = 消息重传时间
        self.消息重传最大次数 = 消息重传最大次数
        self.writer = writer
        self.心跳间隔 = 心跳间隔
        self.会话ID = 会话ID
        self.当前消息: UDP消息 | None = None
        self.chacha20 = ChaCha20(密码)
        self.loop = asyncio.get_running_loop()

    def connection_made(self, 传输: asyncio.DatagramTransport):
        self.传输 = 传输
        self.主任务 = self.loop.create_task(self.主循环())
        self.心跳 = UDP心跳(传输, self.会话ID, self.心跳间隔)
        self.心跳任务 = self.loop.create_task(self.心跳())

    def datagram_received(self, 数据: bytes, 地址: Tuple[str, int]):
        消息 = UDP消息.拆包(数据, 地址)
        self.心跳.刷新接收()
        # 确认消息
        if 消息.消息类型 == UDP消息类型.确认收到 and self.当前消息 is not None:
            if self.当前消息.确认收到(消息.获取确认的消息ID()):
                self.当前消息 = None
        # 数据包
        elif 消息.消息类型 == UDP消息类型.数据:
            try:
                self.writer.write(self.chacha20(消息.内容))
                消息.创建确认消息().发送(self.传输, False)
            except:
                self.关闭()
        # 关闭
        elif 消息.消息类型 == UDP消息类型.关闭:
            self.关闭()

    def error_received(self, 异常):
        self.关闭()

    def connection_lost(self, 异常):
        self.关闭()

    def 关闭(self):
        if self.当前消息 is not None:
            self.当前消息.取消()
        self.writer.close()
        self.传输.close()

    def 发送消息(self, 消息: UDP消息):
        if not self.运行正常():
            raise Exception('链接已关闭')
        消息.内容 = self.chacha20(消息.内容)
        self.当前消息 = 消息
        self.心跳.刷新发送()
        return 消息.发送(self.传输)

    def 运行正常(self):
        return not (self.传输.is_closing() or self.writer.is_closing() or self.心跳.链接断开)

    async def 主循环(self):
        while self.运行正常():
            当前时间 = time.time()
            if self.当前消息 is not None and 当前时间 - self.当前消息.时间辍 >= self.消息重传时间:
                if self.当前消息.重传次数 < self.消息重传最大次数:
                    self.当前消息.发送(self.传输)
                else:
                    self.关闭()
            await asyncio.sleep(0.1)
