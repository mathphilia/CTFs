import re, socket, time
import random

sock = socket.socket()
sock.connect(('be.ax', 31100))
time.sleep(1)

recv = sock.recv(1 << 16).decode()
n = int(re.findall(r'n = \d+', recv)[0].split()[-1])
e = int(re.findall(r'e = \d+', recv)[0].split()[-1])
ct = int(re.findall(r'ct = \d+', recv)[0].split()[-1])

while True:
    mul = random.getrandbits(n.bit_length())
    _ct = pow(mul, e, n) * ct % n
    sock.send(str(_ct).encode() + b'\n')
    time.sleep(1)
    recv = sock.recv(1 << 16).decode()
    number = re.findall(r'\d+', recv)
    if number:
        break

_flag = int(number[0].split()[-1])
flag = _flag * pow(mul, -1, n) % n
flag = flag.to_bytes((flag.bit_length() + 7) // 8, 'big')[16:-16]
print(flag)
