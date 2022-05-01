import re, socket, time

sock = socket.socket()
sock.connect(('phe1.cpctf.space', 30007))

time.sleep(1)
recv = sock.recv(1 << 16).decode()
N = int(re.findall(r'N = \d+', recv)[0][3:])
enc_a = int(re.findall(r'encrypt\(a\) = \d+', recv)[0][13:])
enc_b = int(re.findall(r'encrypt\(b\) = \d+', recv)[0][13:])
ans = enc_a * enc_b % N

sock.send(str(ans).encode() + b'\n')
time.sleep(1)
print(sock.recv(1 << 16).decode())
