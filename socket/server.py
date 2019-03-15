#!/usr/bin/python3

import socket

import sys

#（1）创建socket对象

serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#（2）获取本地主机名

host = socket.gethostname()

#（3）设置端口号

port = 9999

#（4）绑定端口号

serversocket.bind((host, port))

#（5）设置最大连接数，超过后排队

serversocket.listen(5)

while True:

    # 建立客户端连接

    clientsocket, addr = serversocket.accept()

    print("连接地址：%s" % str(addr))
    # print(addr)
    # print(clientsocket)

    message = "欢迎访问博客！" + "\r\n"

    clientsocket.send(message.encode('utf-8'))

    clientsocket.close()

