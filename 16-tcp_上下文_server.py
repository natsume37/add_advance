# coding : utf-8
# 夏目&青一
# @name:tcp_上下文_client
# @time: 2023/6/4  0:57
import socket
import asyncio


async def waiter(conn, loop):
    while True:
        try:
            data = await loop.sock_recv(conn, 1024)
            if not data:
                break
            await loop.sock_sendall(conn, data.upper())
        except ConnectionResetError:
            break
    conn.close()




async def main(ip, port):
    server = socket.socket()
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server.bind((ip, port))
    server.listen(5)
    server.setblocking(False)
    loop = asyncio.get_running_loop()
    while True:
        conn, addr = await loop.sock_accept(server)
        # 创建事件循环
        loop.create_task(waiter(conn, loop))


asyncio.run(main('localhost',8090))




