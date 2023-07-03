import re, socket, time
import hashlib
from Crypto.Cipher import AES


sock = socket.socket()
sock.connect(('group-projection.chal.uiuc.tf', 1337))
time.sleep(2)

recv = sock.recv(1 << 16).decode()
g = int(re.findall(r'g = \d+', recv)[0].split()[-1])
p = int(re.findall(r'p = \d+', recv)[0].split()[-1])
A = int(re.findall(r'A = \d+', recv)[0].split()[-1])

k = p - 1
d = 3
while k % d:
    d += 1
k //= d

sock.send(f'{k}\n'.encode())
time.sleep(1)

recv = sock.recv(1 << 16).decode()
c = int(re.findall(r'c = \d+', recv)[0].split()[-1])
enc = c.to_bytes((c.bit_length() + 7) // 8, 'big')

for i in range(d):
    S = pow(g, i * k, p)
    key = S.to_bytes((S.bit_length() + 7) // 8, 'big')
    key = hashlib.md5(key).digest()
    cipher = AES.new(key, AES.MODE_ECB)
    flag = int.from_bytes(cipher.decrypt(enc), 'big')
    if flag.startswith(b'uiuctf'):
        print(flag)