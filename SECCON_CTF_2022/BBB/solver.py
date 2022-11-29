import re, socket, time

def sqrtp(a, p):
    # solve "x ** 2 - a = 0 (mod p)"
    if pow(a, (p - 1) // 2, p) == p - 1:
        return
    elif pow(a, (p - 1) // 2, p) == 0:
        return 0
    k, n =(p - 1) // 2, 1
    while k % 2 == 0:
        k //= 2
        n += 1
    m = 2
    while pow(m, (p - 1) // 2, p) == 1:
        m += 1
    w, x, y, z = n, pow(m, k, p), pow(a, k, p), pow(a, (k + 1) // 2, p)
    while y != 1:
        Y = y
        for w_new in range(1, w + 1):
            Y = pow(Y, 2, p)
            if Y == 1:
                break
        assert w_new < w
        sqrtx = pow(x, 1 << w - w_new - 1, p)
        w = w_new
        x = pow(sqrtx, 2, p)
        y = y * pow(sqrtx, 2, p) % p
        z = z * sqrtx % p
    return z

def quadratic(a, b, p):
    # solve "x ** 2 + a * x + b = 0 (mod p)"
    if a % 2 != 0:
        a += p
    sqrtD = sqrtp((a // 2) ** 2 - b, p)
    if sqrtD is None:
        return None,
    return (-a // 2 + sqrtD) % p, (-a // 2 - sqrtD) % p

def CRT(remainders, moduli):
    assert len(remainders) == len(moduli)
    if len(remainders) == 1:
        return remainders[0], moduli[0]
    if len(remainders) == 2:
        a, b = remainders
        m, n = moduli
        rem = pow(m, -1, n) * m * b + pow(n, -1, m) * n * a
        return rem % (m * n), m * n
    if 2 < len(remainders):
        rem, mod = CRT(remainders[1:], moduli[1:])
        return CRT((remainders[0], rem), (moduli[0], mod))

def nth_root(x, n):
    d = x.bit_length() // n
    ret = 0
    for i in range(d, -1, -1):
        ret ^= 1 << i
        if x < ret ** n:
            ret ^= 1 << i
    return ret


sock = socket.socket()
sock.connect(('BBB.seccon.games', 8080))
time.sleep(.1)

recv = sock.recv(1 << 16).decode()
a = int(re.findall(r'a=\d+', recv)[0][2:])
p = int(re.findall(r'p=\d+', recv)[0][2:])

e = 11
b = (e - a * e - e ** 2) % p
seeds= {e}
length = 1
while length < 5:
    tmp = set(seeds)
    for seed in tmp:
        seeds.update(quadratic(a, b - seed, p))
    if None in seeds:
        seeds.remove(None)
    length = len(seeds)
    if len(tmp) == length:
        print('failed to hack')
        exit()

sock.send(str(b).encode() + b'\n')
for seed in seeds:
    sock.send(str(seed).encode() + b'\n')

time.sleep(20)
recv = sock.recv(1 << 16).decode()
lst = re.findall(r'n=\d+', recv)
moduli = [int(n[2:]) for n in lst]
lst = re.findall(r': \d+', recv)
ciphertexts = [int(ct[2:]) for ct in lst]

plaintext = nth_root(CRT(ciphertexts, moduli)[0], e)
print(bytes.fromhex(hex(plaintext)[2:]))