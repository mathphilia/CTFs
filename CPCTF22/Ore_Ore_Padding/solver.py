# This solution fails once in twice probably because of challenge program.

import re, socket, time

sock = socket.socket()
sock.connect(('ore-ore-padding.cpctf.space', 30003))

time.sleep(.3)
recv = sock.recv(1 << 16).decode()
n = int(re.findall('n = .+', recv)[0][3:], 16)
e = int(re.findall('e = .+', recv)[0][3:], 16)
c = int(re.findall('c = .+', recv)[0][3:], 16)

for _ in range(n.bit_length()):
    sock.send(str(c).encode() + b'\n')
    c = c * pow(2, e, n) % n

time.sleep(10)
recv = sock.recv(1 << 16).decode()
result = re.findall('ok|error', recv)

k = int(''.join('0' if msg == 'ok' else '1' for msg in result), 2) + 1
m = (k * n) >> n.bit_length()
print(m.to_bytes((m.bit_length() + 7) // 8, 'big'))
