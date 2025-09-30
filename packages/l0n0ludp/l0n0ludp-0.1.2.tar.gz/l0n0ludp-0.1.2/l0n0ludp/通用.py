import argparse
from .UDP消息 import UDP消息, UDP消息类型


class UDP服务器信息:
    监听地址: str
    监听端口: int
    服务器地址: str
    服务器端口: int
    密码: str
    消息重传时间: float = 0.5
    消息重传最大次数: int = 3
    心跳间隔 = 2.0
    使用uvloop = True


def 读取参数():
    parser = argparse.ArgumentParser(description="启动UDP服务器并连接远端")
    parser.add_argument("listen_host", help="本地监听地址")
    parser.add_argument("listen_port", type=int, help="本地监听端口")
    parser.add_argument("server_host", help="远程服务器地址")
    parser.add_argument("server_port", type=int, help="远程服务器端口")
    parser.add_argument("password", help="通信密码")
    parser.add_argument("--interval", type=float, default=2.0, help="心跳间隔(秒)")
    parser.add_argument("--resend-time", type=float,
                        default=1.0, help="消息重传时间(秒)")
    parser.add_argument("--max-resend-times", type=int,
                        default=3, help="消息重传最大次数(次)")
    parser.add_argument("--no-uvloop", action="store_false",
                        default=True, help="启用调试模式")
    args = parser.parse_args()

    UDP服务器信息.监听地址 = args.listen_host
    UDP服务器信息.监听端口 = args.listen_port
    UDP服务器信息.服务器地址 = args.server_host
    UDP服务器信息.服务器端口 = args.server_port
    UDP服务器信息.密码 = args.password
    UDP服务器信息.心跳间隔 = args.interval
    UDP服务器信息.消息重传时间 = args.resend_time
    UDP服务器信息.消息重传最大次数 = args.max_resend_times
    UDP服务器信息.使用uvloop = not args.no_uvloop


async def tcp读取任务(cls, *args):
    try:
        while cls.运行正常():
            data = await cls.reader.read(512)
            if not data:
                break
            消息 = UDP消息(UDP消息类型.数据, cls.会话ID, data, None, cls.UDP地址)
            await cls.UDP协议.发送消息(消息, *args)
    except:
        pass


def 使用uvloop():
    import uvloop
    uvloop.install()
