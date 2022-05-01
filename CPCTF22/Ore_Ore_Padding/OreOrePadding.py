from Crypto.Util.number import *
from Crypto.Random import get_random_bytes
from secret import FLAG

p = getPrime(512)
q = getPrime(512)
n = p * q
phi = (p - 1) * (q - 1)
e = 0x10001
d = pow(e, -1, phi)

def encrypt(plaintext):
    m = padding(plaintext)
    c = pow(m, e, n)
    return c

def padding(plaintext):
    remain = 128 - len(plaintext)
    m = 0
    while m < n // 2:
        plaintext = get_random_bytes(remain - 1) + b'\x00' + plaintext
        m = bytes_to_long(plaintext)
    return m

def decrypt(c):
    m = pow(c, d, n)
    plaintext = long_to_bytes(m)
    if m < n // 2:
        return b'ok'
    else:
        return b'padding error'

c = encrypt(FLAG)

print(f"n = {hex(n)}")
print(f"e = {hex(e)}")
print(f"c = {hex(c)}")

print("")
while True:
    cipher = input("input : ")
    try:
        cipher = int(cipher)
    except ValueError:
        break
    print(decrypt(cipher))
print("Thank you")

