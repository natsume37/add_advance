# coding : utf-8
# 夏目&青一
# @name:多IO复用
# @time: 2023/5/24  20:43

import select
import socket

server = socket.socket()
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server.bind(('127.0.0.1', 8080))
server.listen(5)
server.setblocking(False)

input_server = [server]
while True:
    rlist, wlist, xlist = select.select(input_server, [], [])
    for i in rlist:
        if i is server:
            conn, addr = i.accept()
            input_server.append(conn)
            continue
        try:
            data = i.recv(1024)
            if not data:
                i.close()
                input_server.remove(i)
                continue
            i.send(data.upper())
        except ConnectionResetError:
            i.close()
            input_server.remove(i)
            continue


