import random, re, socket, time

sock = socket.socket()
sock.connect(('challs.m0lecon.it', 1753))
time.sleep(.5)
recv=sock.recv(1<<16).decode()

n = int(re.findall(r'n = \d+', recv)[0][4:])
e = int(re.findall(r'e = \d+', recv)[0][4:])
c = int(re.findall(r'c = \d+', recv)[0][4:])

for _ in range(10):
    sock.send(str(random.getrandbits(100)).encode() + b'\n')
    time.sleep(.5)
    recv = sock.recv(1 << 16).decode()

    phi=int(re.findall(r'M = \d+', recv)[0][4:])
    d=pow(e, -1, phi)
    m=pow(c, d, n)
    print(m.to_bytes((m.bit_length() + 7) // 8, 'big'))
