import re, socket, time

def answer(x = None, y = None):
    # auguments are the bit length of each variable
    if x is None:
        y = 1 << (y - 1)
        x = r * pow(s, -1, q) * y % q
    else:
        x = 1 << (x - 1)
        y = s * pow(r, -1, q) * x % q
    return x, y

sock = socket.socket()
sock.connect(('04.cr.yp.toc.tf', 13777))

sock.send(b'G\n')
time.sleep(1)
recv = sock.recv(1 << 16).decode()
print(recv)
q = int(re.findall(r'q = \d+', recv)[-1][4:])
r = int(re.findall(r'r = \d+', recv)[-1][4:])
s = int(re.findall(r's = \d+', recv)[-1][4:])

sock.send(b'S\n')
while True:
    time.sleep(.1)
    recv = sock.recv(1 << 16).decode()
    print(recv)
    restriction = re.findall(r'. is \d+-bit', recv)[-1]
    var, nbits = restriction[0], int(restriction[5:-4])
    x, y = answer(**{var: nbits})
    sock.send(f'{x}, {y}\n'.encode())
