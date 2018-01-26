# server.py

import socket
import os

server = socket.socket()

ip_port = ("localhost", 6969)

server.bind(ip_port)

server.listen()
print("服务器监听开启")

while True:
    conn, addr = server.accept()

    print("客户端已连接：", addr)
    while True:
        data = conn.recv(1024)
        if not data:
            print("client close...")
            break

        print("客户端信息：", data.decode("utf-8"))

        conn.send(data)

conn.close()