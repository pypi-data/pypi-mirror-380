import asyncio
import time
from .UDP消息 import UDP消息, UDP消息类型
from .通用 import tcp读取任务
from .UDP心跳 import UDP心跳
from .ChaCha20 import ChaCha20
from typing import Tuple, Dict


class 远端UDP服务器协议(asyncio.DatagramProtocol):
    def __init__(
            self,
            消息重传时间: float,
            消息重传最大次数: int,
            服务器地址: str,
            服务器端口: int,
            心跳间隔: float,
            密码: str):
        self.消息重传时间 = 消息重传时间
        self.消息重传最大次数 = 消息重传最大次数
        self.服务器地址 = 服务器地址
        self.服务器端口 = 服务器端口
        self.心跳间隔 = 心跳间隔
        self.chacha20 = ChaCha20(密码)
        self.会话TCP客户端: Dict[int, TCP客户端] = {}
        self.loop = asyncio.get_running_loop()

    def connection_made(self, 传输: asyncio.DatagramTransport):
        self.传输 = 传输

    def datagram_received(self, 数据: bytes, 地址: Tuple[str, int]):
        消息 = UDP消息.拆包(数据, 地址)
        tcp客户端 = self.获取tcp客户端(消息.会话ID)
        tcp客户端.UDP地址 = 地址
        if hasattr(tcp客户端, '心跳'):
            tcp客户端.心跳.刷新接收()
        # 确认消息
        if 消息.消息类型 == UDP消息类型.确认收到 and tcp客户端.当前消息 is not None:
            if tcp客户端.当前消息.确认收到(消息.获取确认的消息ID()):
                tcp客户端.当前消息 = None
        # 转发数据
        elif 消息.消息类型 == UDP消息类型.数据:
            try:
                tcp客户端.发送消息(self.chacha20(消息.内容))
                消息.创建确认消息().发送(self.传输, False)
            except Exception as e:
                tcp客户端.关闭()
        # 关闭会话
        elif 消息.消息类型 == UDP消息类型.关闭:
            tcp客户端.关闭()

    def error_received(self, 异常):
        self.关闭()

    def connection_lost(self, 异常):
        self.关闭()

    def 运行正常(self):
        return not (self.传输.is_closing())

    def 关闭(self):
        for tcp客户端 in self.会话TCP客户端.values():
            tcp客户端.关闭()
        self.传输.close()

    def 获取tcp客户端(self, 会话ID: int):
        tcp客户端 = self.会话TCP客户端.get(会话ID)
        if tcp客户端 is None:
            tcp客户端 = TCP客户端(
                self, 会话ID, self.服务器地址,
                self.服务器端口, self.心跳间隔)
            self.会话TCP客户端[会话ID] = tcp客户端
        return tcp客户端

    def 发送消息(self, 消息: UDP消息, tcp客户端):
        if not self.运行正常():
            raise Exception('链接已关闭')
        消息.内容 = self.chacha20(消息.内容)
        tcp客户端.当前消息 = 消息
        tcp客户端.心跳.刷新发送()
        return 消息.发送(self.传输)

    async def 主循环(self):
        while self.运行正常():
            当前时间 = time.time()
            for tcp客户端 in self.会话TCP客户端.values():
                if tcp客户端.当前消息 is None:
                    continue
                if 当前时间 - tcp客户端.当前消息.时间辍 < self.消息重传时间:
                    continue
                if tcp客户端.当前消息.重传次数 >= self.消息重传最大次数:
                    tcp客户端.关闭()
                tcp客户端.当前消息.发送(self.传输)

            await asyncio.sleep(0.1)


class TCP客户端:
    def __init__(
            self,
            UDP协议: 远端UDP服务器协议,
            会话ID: int,
            服务器地址: str,
            服务器端口: int,
            心跳间隔: float):
        self.UDP协议 = UDP协议
        self.会话ID = 会话ID
        self.服务器地址 = 服务器地址
        self.服务器端口 = 服务器端口
        self.心跳间隔 = 心跳间隔
        self.UDP地址: Tuple[str, int] | None = None
        self.当前消息: UDP消息 | None = None
        self.发送缓存 = []
        self.loop = asyncio.get_running_loop()
        self.loop.create_task(self.启动())

    def 关闭(self):
        if hasattr(self, 'writer'):
            self.writer.close()
        if hasattr(self, '读取任务'):
            self.读取任务.cancel()

    def 运行正常(self):
        return not self.writer.is_closing() and self.UDP协议.运行正常() and not self.心跳.链接断开

    async def 启动(self):
        self.reader, self.writer = await asyncio.open_connection(self.服务器地址, self.服务器端口)
        self.读取任务 = self.loop.create_task(tcp读取任务(self, self))
        self.心跳 = UDP心跳(self.UDP协议.传输, self.会话ID, self.心跳间隔, self.UDP地址)
        self.心跳任务 = self.loop.create_task(self.心跳())

        for 数据 in self.发送缓存:
            self.writer.write(数据)

    def 发送消息(self, 数据: bytes):
        if hasattr(self, 'writer'):
            self.writer.write(数据)
        else:
            self.发送缓存.append(数据)
