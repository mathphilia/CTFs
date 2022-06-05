import re, socket, time

p = 2 ** 512 + 0x4b #next prime of 2^512

sock = socket.socket()
sock.connect(('primeparty.quals.beginners.seccon.jp', 1336))
for _ in range(3):
    sock.send(str(p).encode() + b'\n')

time.sleep(2)
recv = sock.recv(1 << 16).decode()

n = int(re.findall(r'n = \d+', recv)[0][4:])
e = int(re.findall(r'e = \d+', recv)[0][4:])
c = int(re.findall(r'cipher = \d+', recv)[0][9:])

d = pow(e, -1, p-1)
m = pow(c, d, p)
print(m.to_bytes((m.bit_length() + 7) // 8, 'big'))
