import re, socket, time

def sqrt_minus1(modulus):
    #return x such that pow(x, 2, modulus) == -1
    if modulus % 4 != 1:
        return
    for n in range(2, modulus):
        if pow(n, (modulus - 1) // 2, modulus) != 1:
            return pow(n, (modulus - 1) // 4, modulus)

def minimal_residue(n, modulus):
    if (n % modulus) * 2 < modulus:
        return n % modulus
    else:
        return n % modulus - modulus

def SOTS(p):
    x = sqrt_minus1(p)
    y = 1
    k = (x ** 2 + y ** 2) // p
    while 1 < k:
        xx, yy = minimal_residue(x, k), minimal_residue(y, k)
        k_new = (xx ** 2 + yy ** 2) // k
        x, y, k = (x * xx + y * yy) // k,(x * yy - y * xx) // k, k_new
    return x, y


sock = socket.socket()
sock.connect(('05.cr.yp.toc.tf', 37331))
sock.send(b'G\nS\n')

time.sleep(1)
recv = sock.recv(1 << 16).decode()
N = int(re.findall(r'n = \d+', recv)[0][3:])
primes = map(int, input(f'input prime factors of {N}\n> ').split())

x,y=1,0
for p in primes:
    _x, _y = SOTS(p)
    x, y = x * _x + y * _y, x * _y - y * _x

sock.send(f'{x}, {y}'.encode() + b'\n')
time.sleep(1)
print(sock.recv(1 << 16).decode())
