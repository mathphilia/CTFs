import re, socket, time

sock = socket.socket()
sock.connect(('choice.beginners.seccon.games', 1336))

time.sleep(1)
recv = sock.recv(1 << 16).decode()
n = int(re.findall(r'n = \d+', recv)[0].split()[-1])
e = int(re.findall(r'e = \d+', recv)[0].split()[-1])
c = int(re.findall(r'c = \d+', recv)[0].split()[-1])
s = int(re.findall(r's = \d+', recv)[0].split()[-1])

for i in range(4):
    sock.send(str(n + i).encode() + b'\n')

time.sleep(16)
recv = sock.recv(1 << 16).decode()
powers = [int(power.split()[-1]) for power in re.findall(r'result_a : \d+', recv)]
t = (powers[3] + s * powers[1] - n * powers[0]) * pow(powers[2], -1, n) % n

# solve x ** 3 - t * x ** 2 + s * x - n = 0
p = 0
while True:
    _p = p
    p -= (p ** 3 - t * p ** 2 + s * p - n) // (3 * p ** 2 - 2 * t * p + s)
    if _p == p:
        break

diff = 0
while True:
    p = _p - diff
    if p ** 3 - t * p ** 2 + s * p - n == 0:
        break
    p = _p + diff
    if p ** 3 - t * p ** 2 + s * p - n == 0:
        break
    diff += 1

# solve x ** 2 - (p + q) * x + (p * q) = 0
tt = t - p
nn = n // p
q = 0
while True:
    _q = q
    q -= (q ** 2 - tt * q + nn) // (2 * q - tt)
    if _q == q:
        break

diff = 0
while True:
    q = _q - diff
    if q ** 2 - tt * q + nn == 0:
        break
    q = _q + diff
    if q ** 2 - tt * q + nn == 0:
        break
    diff += 1

r = nn // q
phi = (p - 1) * (q - 1) * (r - 1)
d = pow(e, -1, phi)
m = pow(c, d, n)

print(m.to_bytes((m.bit_length() + 7) // 8, 'big'))