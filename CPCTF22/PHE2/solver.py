import re, socket, time

sock = socket.socket()
sock.connect(('phe2.cpctf.space', 30008))

time.sleep(.5)
recv = sock.recv(1 << 16).decode()
n = int(re.findall(r'n = \d+', recv)[0][3:])
g = int(re.findall(r'g = \d+', recv)[0][3:])

c = pow(g, n - 100, n * n)
sock.send(str(c).encode() + b'\n')
time.sleep(.5)
print(sock.recv(1 << 16).decode())
