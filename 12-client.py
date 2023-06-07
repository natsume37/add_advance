# coding : utf-8
# 夏目&青一
# @name:05-tcp_客户端
# @time: 2023/5/24  11:55

import socket

client = socket.socket()
client.connect(('127.0.0.1', 8080))


while True:
    client.send(b'hello')
    data = client.recv(1024)
    print(data)