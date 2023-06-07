# coding : utf-8
# 夏目&青一
# @name:tcp_并发
# @time: 2023/5/24  11:44

import socket

server = socket.socket()
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server.bind(('127.0.0.1', 8990))
server.listen(5)
server.setblocking(False)  # 将所有的阻塞变为非阻塞

c_list = []
d_list = []
while True:
    try:
        conn, addr = server.accept()
        c_list.append(conn)
    except BlockingIOError:
        for conn in c_list:
            try:
                data = conn.recv(1024)
                if not data:
                    conn.close()
                    d_list.append(conn)
                conn.send(data.upper())
            except BlockingIOError:
                pass
            except ConnectionResetError:
                conn.close()
                d_list.append(conn)
        for conn in  d_list:
            c_list.remove(conn)
        d_list.clear()
