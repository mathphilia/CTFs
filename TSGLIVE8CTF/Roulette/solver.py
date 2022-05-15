import re, socket, time

while True:
    sock = socket.socket()
    sock.connect(('chall.live.ctf.tsg.ne.jp', 61234))
    sock.send(b'1\n' * 6)

    time.sleep(1)
    recv = sock.recv(1 << 16).decode()
    x = [int(i[7:]) for i in re.findall(r'Result: \d+', recv)]

    if x[0] != x[1]:
        p = (x[1] - x[2]) * pow(x[0] - x[1], -1, 37) % 37
    else:
        continue
    q = (x[1] - p * x[0]) % 37

    guess = x[-1]
    for i in range(4):
        sock.send(str(36 ** i).encode() + b'\n')
        guess = (guess * p + q) % 37
        sock.send(str(guess).encode() + b'\n')

    time.sleep(1)
    recv = sock.recv(1 << 16).decode()
    if 'Good job' in recv:
        print(recv)
        break
