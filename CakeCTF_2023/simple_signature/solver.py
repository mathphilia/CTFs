import re, socket, time
import hashlib

magic_word = 'cake_does_not_eat_cat'
cigam_word = 'cake_does_eat_cat'
def h(m):
    return int(hashlib.sha512(m.encode()).hexdigest(), 16)


sock = socket.socket()
sock.connect(('crypto.2023.cakectf.com', 10444))
sock.send(f'S\n{cigam_word}\n'.encode())
time.sleep(1)

recv = sock.recv(1 << 16).decode()
p = int(re.findall(r'p = \d+', recv)[0].split()[-1])
g = int(re.findall(r'g = \d+', recv)[0].split()[-1])
w, v = map(int, re.findall(r'vkey = \((\d+), (\d+)\)', recv)[0])
s, t = map(int, re.findall(r'\(s, t\) = \((\d+), (\d+)\)', recv)[0])

power = (h(magic_word) - h(cigam_word)) * pow(-v, -1, p - 1) % (p - 1)
t = t * pow(g, power, p) % p
sock.send(f'V\n{magic_word}\n{s}\n{t}\n'.encode())
time.sleep(1)

recv = sock.recv(1 << 16).decode()
print(recv)