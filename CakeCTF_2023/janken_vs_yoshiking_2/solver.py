import re, socket, time
import json, numpy

size = 5
def matrix_parse(lst):
    return numpy.matrix([lst[i:i + size] for i in range(0, len(lst), size)])


def matrix_pow(mat, power, mod):
    tmp = mat ** 1
    result = mat ** 0
    while power:
        if power & 1:
            result = result * tmp % mod
        tmp = tmp * tmp % mod
        power >>= 1
    return result


sock = socket.socket()
sock.connect(('crypto.2023.cakectf.com', 10555))
time.sleep(1)

recv = sock.recv(1 << 16).decode()
p = int(re.findall(r'p: \d+', recv)[0][3:])
M = json.loads(re.findall(r'M: [\[\d, \]]+', recv)[0][3:])
M = matrix_parse(M)
E = M ** 0

mat = numpy.matrix(M)
order = 1
for k in range(size):
    if numpy.all(mat == E):
        break
    order *= p ** size - p ** k
    mat = matrix_pow(mat, p ** size - p ** k, p)

while order % 3 == 0:
    order //= 3

time.sleep(2)
mat = matrix_pow(M, order, p)
while not numpy.all(mat == E):
    order *= 3
    mat = matrix_pow(mat, 3, p)

rock = matrix_pow(M, 0 * order // 3, p)
scissors = matrix_pow(M, 1 * order // 3, p)
paper = matrix_pow(M, 2 * order // 3, p)
def decide_hand(commitment):
    C_pow = matrix_pow(commitment, order // 3, p)
    if numpy.all(C_pow == rock):
        return 3 # paper
    elif numpy.all(C_pow == scissors):
        return 1 # rock
    elif numpy.all(C_pow == paper):
        return 2 # scissors
    else:
        raise RuntimeError


for _ in range(100):
    C = json.loads(re.findall(r'my commitment is=[\[\d, \]]+', recv)[0].split('=')[-1])
    C = matrix_parse(C)
    hand = decide_hand(C)
    sock.send(f'{hand}\n'.encode())
    time.sleep(0.1)
    recv = sock.recv(1 << 16).decode()

print(recv)