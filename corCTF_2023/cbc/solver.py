import string

alphabet = string.ascii_uppercase

def sub_key(block1, block2):
    index1 = [alphabet.index(c) for c in block1]
    index2 = [alphabet.index(c) for c in block2]
    return ''.join(alphabet[(i1 - i2) % len(alphabet)] for i1, i2 in zip(index1, index2))


with open('cbc_output.txt') as f:
    iv = f.readline().split()[-1][1:-1]
    ct = f.readline().split()[-1][1:-1]

klen = len(iv)
Vigenere = ''
blocks = [ct[i:i + klen] for i in range(0, len(ct), klen)]
prev_block = iv
for block in blocks:
    Vigenere += sub_key(block, prev_block)
    prev_block = block

print(Vigenere)
print()

key = 'ACXQTSTCSXZWFCZY' # https://www.dcode.fr/vigenere-cipher
plaintext = ''
for i in range(0, len(Vigenere), klen):
    plaintext += sub_key(Vigenere[i:i + klen], key)
    
print(plaintext)