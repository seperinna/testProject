#coding=utf-8
import socket

# 建立TCP连接，1）IP地址 2）端口号
ip="172.16.72.9"     #服务器端ip
port=8080    #服务器端端口
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect((ip,port))

# 传输内容
s.send("hello from client")

# 关闭连接
s.close()