import re, socket, time
from itertools import permutations as perm

answer = []
tmp = tuple()
for n in range(3, 41):
    if n % 3 == 1:
        answer.append('TINP')
        continue
    _add = [i for i in range(1, 1 + n) if i not in tmp]
    for add in perm(_add):
        p = tmp + add
        if sum((-2) ** i * j for i, j in enumerate(p)) == 0:
            answer.append(str(p)[1:-1])
            tmp = p[:-4]
            break

sock = socket.socket()
sock.connect(('02.cr.yp.toc.tf', 13771))
sock.send('\n'.join(answer).encode() + b'\n')

time.sleep(.5)
recv = sock.recv(1 << 16).decode()
print(re.findall(r'CCTF\{.+\}', recv)[0])
