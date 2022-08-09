from itertools import product
from string import printable

def xor(a, b):
    return bytes(i ^ j for i, j in zip(a, b))


with open('out.txt', 'rb') as f:
    enc = f.read()

_key = xor(b'ictf{', enc[:5])
for x in range(256):
    if enc[5] ^ x not in printable.encode():
        continue
    for y in range(256):
        if enc[6] ^ y not in printable.encode():
            continue
        for z in range(256):
            if enc[7] ^ z not in printable.encode():
                continue
            key = int.from_bytes(_key + bytes([x, y, z]), 'little')
            key_stream = b''
            for i in range(6):
                key_stream += pow(key, 2 ** i, 1 << 64).to_bytes(8, 'little')
            flag = xor(enc, key_stream)
            if flag.endswith(bytes(6)):
                print(flag)
