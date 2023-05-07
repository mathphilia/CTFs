p = 3
q = 5
n = p * q
e = 65535
c = 10

for m in range(n):
    if pow(m, e, n) == c:
        print('FLAG{THE_ANSWER_IS_' + str(m) + '}')