import re, socket, time
import json

sock = socket.socket()
sock.connect(('guess-mis.wanictf.org', 50018))

response = []
for i in range(14):
    sock.send(b'1\n')
    sock.send(' '.join(str(j) for j in range(10000) if j & (1 << i)).encode() + b'\n')
    time.sleep(0.5)
    recv = sock.recv(1<<16).decode()
    res = json.loads(re.findall(r'\[[0-9, ]+\]', recv)[0])
    response.append(res)

ANSWER = [None] * 10000
for n in range(10000):
    j = 0
    for i in range(14):
        if n in response[i]:
            j |= 1<<i
    ANSWER[j] = n

sock.send(b'2\n')
sock.send(' '.join(str(n) for n in ANSWER).encode() + b'\n')
time.sleep(0.5)
print(sock.recv(1<<16).decode())