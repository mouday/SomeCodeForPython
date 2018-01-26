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
            print("客户端已断开")
            break

        cmd = data.decode("utf-8")
        print("客户端信息：", cmd)
        res = os.popen(cmd).read()
        print(res)

        if len(res) == 0 :res = "没有返回"

        conn.send(res.encode("utf-8"))

conn.close()