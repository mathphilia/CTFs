import math, sympy

with open('out.txt') as f:
    n = int(f.readline()[4:])
    e = int(f.readline()[4:])
    c = int(f.readline()[4:])

primes = sympy.factorint(n)
phi = math.prod(p - 1 for p in primes)
d = pow(e, -1, phi)
m = pow(c, d, n)
print(m.to_bytes((m.bit_length() + 7) // 8, 'big'))