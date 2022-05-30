import re, socket, time

sock = socket.socket()
sock.connect(('simple-service-c45xrrmhuc5su.shellweplayaga.me', 31337))
ticket = b'ticket{  }\n' # YOUR TICKET

sock.send(ticket)
time.sleep(1)
recv = sock.recv(1 << 16).decode()

print(recv)
a, b = map(int, re.findall(r'\d+', recv))
sock.send(str(a + b).encode() + b'\n')

time.sleep(1)
recv = sock.recv(1 << 16).decode()
print(recv)
