from output import cipher
import itertools, re

available = re.findall('[a-zA-Z0-9!-/:-?\[-`|~]', bytes(range(128)).decode())
available = [ord(c) for c in available]
key = [[*range(256)] for _ in range(16)]

for i, plain in enumerate(b'TSGCTF{'):
    key[i] = [plain ^ cipher[i]]

for i, plain in enumerate(b'==}'):
    key[i - 3] = [plain ^ cipher[i - 3]]

key[-4] = [k for k in key[-4] if k ^ cipher[-4] in b'AQgw']

for i in range(7,13):
    key[i] = [k for k in key[i] if all(k ^ cip in available for cip in cipher[i::16])]


product = list(itertools.product(*key))
_flag = bytes(product[0][i % 16] ^ c for i, c in enumerate(cipher)).decode()
for i, f in enumerate(_flag):
    if len(key[i % 16]) == 1: #determined digit
        print('\033[31m' + f + '\033[0m', end = '')
    else: #indetermined digit
        print(f, end = '')
print()