import re, socket, time
import base64, hashlib

def xor(*args):
    if len(args) == 1:
        return args[0]
    else:
        return bytes(x ^ y for x, y in zip(xor(*args[:-1]), args[-1]))


sock = socket.socket()
sock.connect(('crypto.2023.cakectf.com', 11111))

sock.send(b'1\n' + base64.b64encode(b'123456789') + b'\n')
time.sleep(1)
recv = sock.recv(1 << 16).decode()
cookie = re.findall(r'your cookie => [0-9A-Za-z\+/=]+', recv)[0].split()[-1]
enc = base64.b64decode(cookie)
d1, d2 = enc[16:32], enc[32:48]

for byte in range(256):
    data0 = bytes([byte]) + b'|user=root|\x04\x04\x04\x04'
    data1 = hashlib.md5(d1).digest()
    data2 = hashlib.md5(d2).digest()
    username_suffix = xor(data0, data1, data2)
    username_base64 = base64.b64encode(b'123456789' + username_suffix)
    sock.send(b'1\n' + username_base64 + b'\n')

time.sleep(1)
recv = sock.recv(1 << 16).decode()
for _cookie in re.findall(r'your cookie => [0-9A-Za-z\+/=]+', recv):
    cookie = _cookie.split()[-1]
    enc = base64.b64decode(cookie)
    IV, d1, d3 = enc[0:16], enc[16:32], enc[48:64]
    sock.send(b'2\n' + base64.b64encode(IV + d1 + d3) + b'\n')

time.sleep(1)
recv = sock.recv(1 << 16).decode()
print(re.findall(r'CakeCTF\{[\x20-\x7e]+\}', recv)[0])