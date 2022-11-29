import math

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


with open('output.txt') as f:
    exec(f.read())

p = math.gcd(c1 + c2, n)
q = math.gcd(c1 - c2, n)
r = n // p // q

phi = (p - 1) * (q - 1) * (r - 1)
d = pow(65537, -1, phi)
m_square = pow(cm, d, n)

m_square_p = m_square % p
m_square_q = m_square % q
m_square_r = m_square % r

m_candidate_p = sqrtp(m_square_p, p)
m_candidate_q = sqrtp(m_square_q, q)
m_candidate_r = sqrtp(m_square_r, r)

for m_p in (m_candidate_p, p - m_candidate_p):
    for m_q in (m_candidate_q, q - m_candidate_q):
        for m_r in (m_candidate_r, r - m_candidate_r):
            m, pqr = CRT((m_p, m_q, m_r), (p, q, r))
            padded = m.to_bytes((m.bit_length() + 7) // 8, 'big')
            if b'SECCON' in padded:
                flag = padded[padded.index(b'SECCON'):]
                print(flag)