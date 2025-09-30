import asyncio
from .本地UDP协议 import 本地UDP客户端协议
from .UDP消息 import UDP消息类型, UDP消息
from .ID生成 import 循环ID生成器
from .通用 import tcp读取任务, 读取参数, UDP服务器信息, 使用uvloop
生成会话ID = 循环ID生成器(0xFFFFFFFF)


class TCP2UDP客户端:
    def __init__(self,
                 reader: asyncio.StreamReader,
                 writer: asyncio.StreamWriter) -> None:
        self.会话ID = 生成会话ID()
        self.reader = reader
        self.writer = writer
        self.loop = asyncio.get_running_loop()
        self.UDP地址 = None

    async def 启动UDP客户端(self):
        self.UDP传输, self.UDP协议 = await self.loop.create_datagram_endpoint(
            lambda: 本地UDP客户端协议(
                UDP服务器信息.消息重传时间,
                UDP服务器信息.消息重传最大次数,
                self.writer,
                UDP服务器信息.心跳间隔,
                self.会话ID,
                UDP服务器信息.密码),
            remote_addr=(UDP服务器信息.服务器地址, UDP服务器信息.服务器端口)
        )

    def 运行正常(self):
        return not (self.writer.is_closing() or self.UDP传输.is_closing())


async def 接待本地TCP客户端(reader: asyncio.StreamReader, writer: asyncio.StreamWriter):
    client = TCP2UDP客户端(reader, writer)
    await client.启动UDP客户端()
    await tcp读取任务(client)
    if not client.UDP传输.is_closing():
        关闭消息 = UDP消息(UDP消息类型.关闭, client.会话ID)
        关闭消息.发送(client.UDP传输, False)


async def 启动本地TCP服务器():
    server = await asyncio.start_server(接待本地TCP客户端, UDP服务器信息.监听地址, UDP服务器信息.监听端口)
    try:
        async with server:
            await server.serve_forever()
    except Exception:
        pass


def main():
    读取参数()
    print(
        f'监听 {UDP服务器信息.监听地址}:{UDP服务器信息.监听端口} -> {UDP服务器信息.服务器地址}:{UDP服务器信息.服务器端口}')
    if UDP服务器信息.使用uvloop:
        使用uvloop()
    try:
        asyncio.run(启动本地TCP服务器())
    except:
        pass


if __name__ == '__main__':
    main()
