import re, socket, time
import hashlib

hashdata = [(str(i), hashlib.sha256(str(i).encode()).digest()) for i in range(1 << 20)]
little = [(i, h) for i, h in hashdata if max(h) < 192]
large = [(i, h) for i, h in hashdata if 64 < min(h)]

found = False
for msg_less, less in little:
    for msg_larger, larger in large:
        if sum(i <= j for i,j in zip(less, larger)) == 32:
            found=True
            break
    if found:
        break

sock = socket.socket()
sock.connect(('mc.ax', 31001))
sock.send(msg_larger.encode().hex().encode() + b'\n')
sock.send(msg_less.encode().hex().encode() + b'\n')
time.sleep(1)

recv = sock.recv(1 << 16).decode()
signature = re.findall(r'here is the signature \(hex\): ([0-9a-f]+)', recv)[0]
signature = [bytes.fromhex(signature[i:i + 64]) for i in range(0, len(signature), 64)]
for i, (n1, n2) in enumerate(zip(larger, less)):
    for _ in range(n1 - n2):
        signature[i] = hashlib.sha256(signature[i]).digest()
signature = b''.join(signature).hex()
sock.send(signature.encode() + b'\n')
time.sleep(1)

print(sock.recv(1 << 16).decode())