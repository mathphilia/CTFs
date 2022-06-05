import re, socket, time

sock = socket.socket()
sock.connect(('command.quals.beginners.seccon.jp', 5555))

sock.send(b'1\nfizzbuzz\n')
time.sleep(1)
recv = sock.recv(1 << 16).decode()

ivenc = re.findall(r'Encrypted command: [0-9a-f]+', recv)[0][len('Encrypted command: '):]
iv, enc = ivenc[:32], ivenc[32:]
iv = int(iv, 16) ^ 0x66697a7a62757a7a0808080808080808 ^ 0x676574666c6167090909090909090909
iv = iv.to_bytes(16, 'big').hex()
sock.send(('2\n' + iv + enc + '\n').encode())

time.sleep(1)
recv = sock.recv(1 << 16).decode()
print(re.findall(r'ctf4b\{.+\}', recv)[0])
