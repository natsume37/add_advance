# coding : utf-8
# 夏目&青一
# @name:13-selectors服务端
# @time: 2023/5/24  23:10

import socket
import selectors


def accept(server):
    conn, addr = server.accept()
    sel.register(conn, selectors.EVENT_READ, read)


def read(conn):
    try:  # windows 版本兼容
        data = conn.recv(1024)
        if not data:
            conn.close()
            sel.unregister(conn)
            return
        conn.send(data.upper())
    except ConnectionResetError:
        conn.close()
        sel.unregister(conn)
        return


server = socket.socket()
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server.bind(('127.0.0.1', 8081))
server.listen(5)
server.setsockopt(False)

sel = selectors.DefaultSelector()
sel.register(server, selectors.EVENT_READ, accept)  # 2设置可读监控  3回调函数

while True:
    events = sel.select()
    for key, mask in events:
        callback = key.data
        callback(key.fileobj)


