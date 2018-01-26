# client.py

import socket

client = socket.socket()

ip_port = ("localhost", 6969)

client.connect(ip_port)

while True:
    content = input(">>:")

    if not content: continue

    client.send(content.encode("utf-8"))

    data = client.recv(1024)

    print("从服务器接收：", data.decode("utf-8"))

client.close()