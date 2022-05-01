import random, re, socket, time

def unBitshiftRightXor(x, shift):
    i = 1
    y = x
    while i * shift < 32:
        z = y >> shift
        y = x ^ z
        i += 1
    return y

def unBitshiftLeftXor(x, shift, mask):
    i = 1
    y = x
    while i * shift < 32:
        z = y << shift
        y = x ^ (z & mask)
        i += 1
    return y

def untemper(x):
    x = unBitshiftRightXor(x, 18)
    x = unBitshiftLeftXor(x, 15, 0xefc60000)
    x = unBitshiftLeftXor(x, 7, 0x9d2c5680)
    x = unBitshiftRightXor(x, 11)
    return x

def predict(values):
    assert 624 <= len(values)
    state = tuple(map(untemper, values[-624:])) + (624,)
    rand = random.Random()
    rand.setstate((3, state, None))
    return rand


sock = socket.socket()
sock.connect(('theluck2.cpctf.space', 30001))

sock.send(b'1\ny\n' * 624)
time.sleep(1)
recv = sock.recv(1 << 16).decode()

result = re.findall(r'is \d+', recv)
result = [int(i[3:]) for i in result]
rand = predict(result)
answer = rand.getrandbits(32)

sock.send(str(answer).encode() + b'\n')
print(sock.recv(1 << 16).decode())
