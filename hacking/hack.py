import itertools
import socket
import sys

ip = sys.argv[1]
port = int(sys.argv[2])
with socket.socket() as client:
    client.connect((ip, port))
    ch = 'abcdefghijklmnopqrstuvwxyz0123456789'
    count = 0
    not_found = True
    i = 1
    while not_found:
        pw_set = itertools.product(ch, repeat=i)
        for p in pw_set:
            pw = ''.join(p)
            client.send(pw.encode())
            count += 1
            response = client.recv(1024)
            response = response.decode()
            if response == 'Connection success!':
                print(pw)
                not_found = False
                break
            elif response == 'Too many attempts':
                not_found = False
                break
        i += 1
