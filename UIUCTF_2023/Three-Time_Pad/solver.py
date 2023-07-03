with open('c1', 'rb') as f:
    c1 = f.read()

with open('c2', 'rb') as f:
    c2 = f.read()

with open('c3', 'rb') as f:
    c3 = f.read()

with open('p2', 'rb') as f:
    p2 = f.read()

key = bytes(a ^ b for a, b in zip(c2, p2))
print(bytes(a ^ b for a, b in zip(key, c1)))
print(bytes(a ^ b for a, b in zip(key, c2)))
print(bytes(a ^ b for a, b in zip(key, c3)))