from gevent import monkey
monkey.patch_all()
from  gevent import spawn
import socket

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
        spawn(comm,conn)

if __name__ == '__main__':
    # run('127.0.0.1', 8080)
    g = spawn(run, '127.0.0.1', 8002)
    g.join()