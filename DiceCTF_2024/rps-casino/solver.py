import re, socket, time
import itertools

def calc_output(byte):
    #calculate the output after 16 steps of LFSR
    #where the last byte of state is `byte`
    state = byte
    ret = 0
    for i in range(4):
        ret += ((state ^ (state >> 1) ^ (state >> 3) ^ (state >> 4)) & 1) << i
        state >>= 1
    return ret

def LFSR(state_list):
    state = 0
    for s in state_list:
        state *= 16
        state += s
    while 1:
        yield state & 0xf
        for i in range(4):
            bit = (state ^ (state >> 1) ^ (state >> 3) ^ (state >> 4)) & 1
            state = (state >> 1) | (bit << 63)

sock = socket.socket()
sock.connect(('mc.ax', 31234))
sock.send(b'rock\n' * 56)
time.sleep(1)

recv = sock.recv(1 << 16).decode()
table = ['Tie!', 'You lose!', 'You win!']
result = re.findall('(' + '|'.join(table) + ')', recv)
result = [table.index(r) for r in result]
output = [tuple(i for i in range(16) if i % 3 == r) for r in result]
candidate = [(o,) for o in output[0]]

print('process takes 5~30 seconds...')
for i in range(1, 16):
    tmp = [x + (y,) for x, y in itertools.product(candidate, output[i])]
    candidate = []
    for cand in tmp:
        if calc_output(cand[-2] + cand[-1] * 16) in output[i + 15]:
            candidate.append(cand)

for cand in candidate:
    rng = LFSR(cand[::-1])
    if all(next(rng) in out for out in output):
        break

hand = [b'rock\n', b'paper\n', b'scissors\n', b'rock\n']
for _ in range(50):
    sock.send(hand[next(rng) % 3 + 1])
time.sleep(2)

print(sock.recv(1 << 16).decode())