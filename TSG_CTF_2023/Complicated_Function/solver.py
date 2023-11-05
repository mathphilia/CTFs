import decimal
decimal.getcontext().prec = 1000

with open('output.txt') as f:
    N = int(f.readline().split()[-1])
    c = int(f.readline().split()[-1])

diff = 2 ** 511 - 3 + 2 ** 1023
while True:
    diff -= 1
    p = (decimal.Decimal(diff ** 2 + 4 * N).sqrt() - diff) / 2
    if p == int(p):
        p = int(p)
        q = N // p
        assert p * q == N
        break

e = 0x10001
phi = (p - 1) * (q - 1)
d = pow(e, -1, phi)
m = pow(c, d, N)
print(m.to_bytes((m.bit_length() + 7) // 8, 'big'))