def nth_root(n, x):
    import random
    result = 1 << (x.bit_length() // n)
    while result ** n != x:
        result -= (result ** n - x) // (n * result ** (n - 1))
        result += random.randrange(-1, 2)
    return result


with open('out.txt') as f:
    n = int(f.readline()[4:])
    e = int(f.readline()[4:])
    c = int(f.readline()[4:])

c = c * pow(5, -100, n) % n
m = nth_root(e, c)
print(m.to_bytes((m.bit_length() + 7) // 8, 'big'))