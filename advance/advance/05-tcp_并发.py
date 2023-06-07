# coding : utf-8
# 夏目&青一
# @name:tcp_并发
# @time: 2023/5/24  11:44

import socket
from threading import Thread


def comm(conn):
    while True:
        try:
            data = conn.recv(1024)
            if not data:
                break
            conn.send(data.upper())
        except:
            break
    conn.close()


def run(ip, port):
    server = socket.socket()  # 默认tcp协议
    server.bind((ip, port))
    server.listen(5)
    while True:
        conn, addr = server.accept()
        Thread(target=comm, args=(conn,)).start()

if __name__ == '__main__':
    run('127.0.0.1', 8080)
