import json, re, string

with open('output.txt') as f:
    N = int(f.readline().split()[-1])
    e = int(f.readline().split()[-1])
    clues = json.loads(f.readline().split(maxsplit = 2)[-1])

table = {}
letters = string.printable
for i, c1 in enumerate(letters):
    for c2 in letters[i + 1:]:
        enc = pow(ord(c1) * ord(c2), e, N)
        table[enc] = table.get(enc, []) + [c1 + c2]

for enc in clues:
    print(table[enc])