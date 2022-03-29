import itertools
import socket
import sys

ip = sys.argv[1]
port = int(sys.argv[2])
with socket.socket() as client:
    client.connect((ip, port))
    found = False
    with open('hacking/passwords.txt') as f:
        for line in f.readlines():
            if found:
                break
            ch_set = []
            for ch in line:
                if ch.isalpha():
                    ch_set.append((ch.lower(), ch.upper()))
                elif ch.isdigit():
                    ch_set.append(tuple(ch))
            pw_set = itertools.product(*ch_set)
            for p in pw_set:
                password = ''.join(p)
                client.send(password.encode())
                response = client.recv(10240).decode()
                if response == 'Connection success!':
                    print(password)
                    found = True
                    break
