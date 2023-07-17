import re, socket, time
import random


##### copy from source code (server.py) #####
def isSquare(a, p):
    return pow(a, (p-1)//2, p) != p-1

class SquareRNG(object):
    def __init__(self, p, sa, sb):
        assert sa != 0 and sb != 0
        (self.p, self.sa, self.sb) = (p, sa, sb)
        self.x = 0

    def int(self, nbits):
        v, s = 0, 1
        for _ in range(nbits):
            self.x = (self.x + 1) % p
            s += pow(self.sa, self.x, self.p) * pow(self.sb, self.x, self.p)
            s %= self.p
            v = (v << 1) | int(isSquare(s, self.p))
        return v

    def bool(self):
        self.x = (self.x + 1) % self.p
        t = (pow(self.sa, self.x, self.p) + pow(self.sb, self.x, self.p))
        t %= self.p
        return isSquare(t, self.p)
##### copy from source code (server.py) #####


p = 20101977534748860053687065956212692207082126595191969411965852652607168559949
sb1 = 1
sb2 = -1

table = {}
for _ in range(256):
    sa = random.randrange(p)
    r1 = SquareRNG(p, sa, sb1)
    rand1 = bin(r1.int(32))[2:].zfill(32)
    r2 = SquareRNG(p, sa, sb2)
    rand2 = bin(r2.int(32))[2:].zfill(32)
    rand = rand1[0] + rand1[11] + rand1[22] + rand1[-1] + rand2[0] + rand2[11] + rand2[22] + rand2[-1]
    rand = rand1[0] + rand1[-1] + rand2[0] + rand2[-1]
    answer = int(r1.bool())
    if rand in table:
        assert table[rand] == answer
    else:
        table[rand] = answer

sock = socket.socket()
sock.connect(('crypto.2023.zer0pts.com', 10666))
sock.send(b'1\n-1\n')

for _ in range(77):
    time.sleep(0.1)
    recv = sock.recv(1 << 16).decode()
    rand1 = int(re.findall(r'0x[0-9a-f]+', recv)[0], 16)
    rand1 = bin(rand1)[2:].zfill(32)
    rand2 = int(re.findall(r'0x[0-9a-f]+', recv)[1], 16)
    rand2 = bin(rand2)[2:].zfill(32)
    rand = rand1[0] + rand1[-1] + rand2[0] + rand2[-1]
    sock.send(str(table[rand]).encode() + b'\n')

time.sleep(0.3)
print(sock.recv(1 << 16).decode())