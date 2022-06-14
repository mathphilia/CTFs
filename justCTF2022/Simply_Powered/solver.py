import re, socket, time
import json, copy

class matrix:
    def __init__(self, lst, mod):
        self.lst = copy.deepcopy(lst)
        self.mod = mod
        self.size = (len(lst), len(lst[0]))
    def one(self):
        return matrix([[i == j for j in range(self.size[1])] for i in range(self.size[0])], self.mod)
    def copy(self):
        return copy.deepcopy(self)
    def __getitem__(self, index):
        return self.lst[index]
    def __mul__(self, other):
        return matrix([[sum(self[i][k] * other[k][j] for k in range(self.size[1])) % self.mod
            for j in range(other.size[1])] for i in range(self.size[0])], self.mod)
    def __pow__(self, other):
        ans = self.one()
        tmp = self.copy()
        while other:
            other, remainder = divmod(other, 2)
            if remainder:
                ans *= tmp
            tmp *= tmp
        return ans
    def __eq__(self, other):
        return self.lst == other.lst

def period(A):
    p = A.mod
    Ap = A ** p
    Apn = Ap
    for i in range(2,100):
        Apn **= p
        if Apn == Ap:
            return p ** i - p
    print('failed to find M')
    exit()
    

sock = socket.socket()
sock.connect(('simply-powered-ams3.nc.jctf.pro', 4444))

for _ in range(100):
    time.sleep(.3)
    recv = sock.recv(1 << 16).decode()
    print(recv)
    e = int(re.findall(r'e =  \d+', recv)[0][3:])
    p = int(re.findall(r'p =  \d+', recv)[0][3:])
    lst = json.loads(re.findall('\[\[.+\]\]', recv)[0])
    M = matrix(lst, p)
    ans = sum(sum(int(k) for k in j) for j in M ** pow(e, -1, period(M)))
    sock.send(str(ans).encode() + b'\n')

recv = sock.recv(1 << 16).decode()
print(recv)
