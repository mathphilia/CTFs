import re, socket, time
import functools, random, sympy


def Brahmagupta(a, b, c, d):
    return a * c + b * d, a * d - b * c

def square_decompose_p(p):
    if p == 2:
        return 1, 1
    assert p % 4 == 1
    for i in range(p):
        if pow(i, (p - 1) // 2, p) == p - 1:
            x = pow(i, (p - 1) // 4, p)
            break
    y = 1
    k = (x ** 2 + y ** 2) // p
    while 1 < k:
        _x = x % k
        xx = _x if _x < k / 2 else _x - k
        _y = y % k
        yy = _y if _y < k / 2 else _y - k
        X, Y = Brahmagupta(x, y, xx, yy)
        x, y = X // k, Y // k
        k = (x ** 2 + y ** 2) // p
    return abs(x), abs(y)

@functools.cache
def factor(n):
    return sympy.factorint(n)

def square_decompose(n):
    x, y = 1, 0
    for p, e in factor(n).items():
        _x, _y = square_decompose_p(p)
        for _ in range(e):
            _y *= (-1) ** random.getrandbits(1)
            x, y = Brahmagupta(x, y, _x, _y)
    return abs(x), abs(y)


sock = socket.socket()
sock.connect(('crypto.2023.zer0pts.com', 10333))
time.sleep(1)

recv=sock.recv(1 << 16).decode()
N=int(re.findall(r'N: \d+',recv)[0].split()[-1])

while True:
    p, q = square_decompose(N)
    if sympy.isprime(p) and sympy.isprime(q):
        sock.send(f'{p}\n{q}\n'.encode() + b'\n')
        break

time.sleep(1)
print(sock.recv(1 << 16).decode())