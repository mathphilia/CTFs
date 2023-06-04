import re, socket, time

sock = socket.socket()
sock.connect(('polyglot4b.beginners.seccon.games', 31416))

with open('solver.jpg', 'rb') as f:
    sock.send(f.read())

time.sleep(1)
print(sock.recv(1 << 16).decode())