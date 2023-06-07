# coding : utf-8
# 夏目&青一
# @name:05-tcp_客户端
# @time: 2023/5/24  11:55
import socket
from threading import Thread, current_thread

def t_client():
    client = socket.socket()
    client.connect(('127.0.0.1', 8002))

    n = 0
    while True:
        msg = f"{current_thread().name} say {n}"
        client.send(msg.encode('utf-8'))
        data = client.recv(1024)
        print(data.decode('utf-8'))
        n += 1

if __name__ == '__main__':
    for _ in range(100):
        Thread(target=t_client).start()