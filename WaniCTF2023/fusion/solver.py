def nth_root(n, x):
    import random
    result = 1 << (x.bit_length() // n)
    while result ** n != x:
        result -= (result ** n - x) // (n * result ** (n - 1))
        result += random.randrange(-1, 2)
    return result


with open('output.txt') as f:
    n = int(f.readline()[4:])
    e = int(f.readline()[4:])
    c = int(f.readline()[4:])
    r = int(f.readline()[4:])

p = r & int('55' * 128, 16)
q = r & int('aa' * 128, 16)
for i in range(1024):
    if p * q % 2 ** (1 + i) != n % 2 ** (1 + i):
        if i & 1:
            p |= 1 << i
        else:
            q |= 1 << i

phi = (p - 1) * (q - 1)
d = pow(e, -1, phi)
m = pow(c, d, n)
print(m.to_bytes((m.bit_length() + 7) // 8, 'big'))