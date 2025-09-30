import struct
import time
import asyncio
from typing import Tuple
from .ID生成 import 循环ID生成器


class UDP消息类型:
    确认收到 = 0
    数据 = 1
    关闭 = 2
    心跳 = 3


生成消息ID = 循环ID生成器(0xFFFFFFFF)


class UDP消息:
    def __init__(
            self,
            消息类型: int,
            会话ID: int,
            内容: bytes | None = None,
            消息ID: int | None = None,
            地址: Tuple[str, int] | None = None):
        self.消息类型 = 消息类型      # 1字节
        self.会话ID = 会话ID          # 4字节
        self.消息ID = 消息ID or 生成消息ID()  # 4字节
        self.内容 = 内容 or b''             # 变长
        self.地址 = 地址
        self.时间辍 = time.time()
        self.重传次数 = -1
        self.封包结果 = None

    def 封包(self) -> bytes:
        if self.封包结果 is None:
            数据长度 = len(self.内容)
            包头 = struct.pack("!B I I H", self.消息类型, self.会话ID, self.消息ID, 数据长度)
            self.封包结果 = 包头 + self.内容
        return self.封包结果

    @classmethod
    def 拆包(cls, 数据: bytes, 来源地址: Tuple[str, int]) -> "UDP消息":
        包头大小 = struct.calcsize("!B I I H")
        包头 = 数据[:包头大小]
        消息类型, 会话ID, 消息ID, 数据长度 = struct.unpack("!B I I H", 包头)
        内容 = 数据[包头大小:包头大小 + 数据长度]
        消息 = cls(消息类型, 会话ID, 内容, 消息ID, 来源地址)
        return 消息

    def __str__(self):
        内容 = self.内容
        if self.消息类型 == UDP消息类型.确认收到:
            消息类型 = '确认收到'
            内容 = self.获取确认的消息ID()
        elif self.消息类型 == UDP消息类型.数据:
            消息类型 = '数据'
        elif self.消息类型 == UDP消息类型.关闭:
            消息类型 = '关闭'
        elif self.消息类型 == UDP消息类型.心跳:
            消息类型 = '心跳'
        return f"([{消息类型}] 会话={self.会话ID} 消息ID={self.消息ID}  内容=[{内容})]"

    def 获取确认的消息ID(self):
        return struct.unpack('!I', self.内容)[0]

    def 发送(self, 传输: asyncio.DatagramTransport, 需要确认: bool = True):
        传输.sendto(self.封包(), self.地址)
        self.时间辍 = time.time()
        self.重传次数 += 1
        if not 需要确认:
            return
        return self.创建确认future()

    def 创建确认消息(self):
        return self.__class__(
            UDP消息类型.确认收到,
            self.会话ID,
            struct.pack('!I', self.消息ID),
            地址=self.地址)

    def 创建确认future(self):
        self.确认future = asyncio.get_running_loop().create_future()
        return self.确认future

    def 确认收到(self, 消息ID: int):
        if self.确认future.done():
            return False
        if self.消息ID != 消息ID:
            return False
        self.确认future.set_result(True)
        return True

    def 取消(self):
        self.确认future.cancel()
