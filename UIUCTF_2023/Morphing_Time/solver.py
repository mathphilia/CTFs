import re, socket, time


sock = socket.socket()
sock.connect(('morphing.chal.uiuc.tf', 1337))
time.sleep(1)

recv = sock.recv(1 << 16).decode()
g = int(re.findall(r'g = \d+', recv)[0].split()[-1])
p = int(re.findall(r'p = \d+', recv)[0].split()[-1])
A = int(re.findall(r'A = \d+', recv)[0].split()[-1])

sock.send(f'{g}\n{A}\n'.encode())
time.sleep(1)

recv = sock.recv(1 << 16).decode()
m = int(re.findall(r'm = \d+', recv)[0].split()[-1])
print(m.to_bytes((m.bit_length() + 7) // 8, 'big'))