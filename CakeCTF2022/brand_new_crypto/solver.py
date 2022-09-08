with open('output.txt') as f:
    lines = f.readlines()

s, t, n = eval(lines[0])
c = eval(lines[1])

table = {pow(m, t - s, n): m for m in range(1,256)}
flag = []

for c1, c2 in c:
    enc = pow(c1, t, n) * pow(c2, -s, n) % n
    flag.append(table[enc])

print(bytes(flag))
