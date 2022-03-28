import socket
import sys

ip = sys.argv[1]
port = int(sys.argv[2])
msg = sys.argv[3]
with socket.socket() as client:
    client.connect((ip, port))
    client.send(msg.encode())
    response = client.recv(1024)
    msg_r = response.decode()
    print(msg_r)