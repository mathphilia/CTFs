def nth_root(n, x):
    import random
    result = 1 << (x.bit_length() // n)
    while result ** n != x:
        result -= (result ** n - x) // (n * result ** (n - 1))
        result += random.randrange(-1, 2)
    return result


with open('output.txt') as f:
    n = int(f.readline())
    e = int(f.readline())
    c = int(f.readline())
    s = int(f.readline())

p_plus_q = s
p_minus_q = nth_root(2, p_plus_q ** 2 - 4 * n)
p = (p_plus_q + p_minus_q) // 2
q = (p_plus_q - p_minus_q) // 2
phi = (p - 1) * (q - 1)
d = pow(e, -1, phi)
m = pow(c, d, n)
print(m.to_bytes((m.bit_length() + 7) // 8, 'big'))