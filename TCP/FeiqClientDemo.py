# coding=utf-8
import socket


ip="localhost"
port=2425
udp=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
# udp.connect((ip,port))
# udp.send('1_lbt4_10#32899#002481627512#0#0#0:1289671407:'
#          'Administrator:PC-201504241459:288:测试消息')
for i in range(5000):
    udp.sendto('1:106:Administrator:PC-201504241459:32:hehehe123',(ip,port))

