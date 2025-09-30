import asyncio
from .远端UDP协议 import 远端UDP服务器协议
from .通用 import 读取参数, UDP服务器信息, 使用uvloop


async def 启动UDP服务器():
    传输, 协议 = await asyncio.get_running_loop().create_datagram_endpoint(
        lambda: 远端UDP服务器协议(
            UDP服务器信息.消息重传时间,
            UDP服务器信息.消息重传最大次数,
            UDP服务器信息.服务器地址,
            UDP服务器信息.服务器端口,
            UDP服务器信息.心跳间隔,
            UDP服务器信息.密码),
        local_addr=(UDP服务器信息.监听地址, UDP服务器信息.监听端口)
    )
    await 协议.主循环()


def main():
    读取参数()
    print(
        f'监听 {UDP服务器信息.监听地址}:{UDP服务器信息.监听端口} -> {UDP服务器信息.服务器地址}:{UDP服务器信息.服务器端口}')

    if UDP服务器信息.使用uvloop:
        使用uvloop()
    try:
        asyncio.run(启动UDP服务器())
    except:
        pass


if __name__ == '__main__':
    main()
