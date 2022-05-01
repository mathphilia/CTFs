c = 810
e = 5
N = 415411

for p in range(2, N):
    if N % p == 0:
        break

q = N // p
phi = (p - 1) * (q - 1)
d = pow(e, -1, phi)
m = pow(c, d, N)

print(m)
