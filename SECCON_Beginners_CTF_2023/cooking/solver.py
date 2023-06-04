import re, socket, time

sock = socket.socket()
sock.connect(('cooking.beginners.seccon.games', 1337))

p = 0xfffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff611
sock.send(str(p).encode() + b'\n')

time.sleep(1)
recv = sock.recv(1 << 16).decode()
meat_pepper = int(re.findall(r'This is meat: \d+', recv)[0].split()[-1])
meat = pow(meat_pepper, pow(3, -1, p - 1), p)

sock.send(f'{meat}\n'.encode() * 17)
time.sleep(1)
print(sock.recv(1 << 16).decode())