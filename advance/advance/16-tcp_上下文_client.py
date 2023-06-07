# coding : utf-8
# 夏目&青一
# @name:tcp_上下文_client
# @time: 2023/6/4  0:57
import socket
import asyncio
class Client(object):
    def __init__(self, ip, port):
        self.ip = ip
        self.port = port
        self.loop = asyncio.get_running_loop()

    async def __aenter__(self):
        self.c = socket.socket()
        # self.c.connect((self.ip,self.port))
        # 异步链接服务器
        await self.loop.sock_connect(self.c, (self.ip, self.port))
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        self.c.close()

    async def recv(self):
        data = await self.loop.sock_recv(self.c, 1024)
        return data

    async def send(self, data):
        await self.loop.sock_sendall(self.c, data.encode('utf-8'))


# 测试
async def main():
    async with Client('127.0.0.1', 8090) as c:
        while True:
            await c.send('abc')
            data = await c.recv()
            print(data)


asyncio.run(main())