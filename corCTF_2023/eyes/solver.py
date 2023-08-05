import json

with open('out.txt') as f:
    p = int(f.readline())
    L = json.loads(f.readline())

flag = (L[0] + L[1] + L[3] - L[2] - L[4] - L[5] + L[6]) % p
flag = flag.to_bytes((flag.bit_length() + 7) // 8, 'big')
print(flag)