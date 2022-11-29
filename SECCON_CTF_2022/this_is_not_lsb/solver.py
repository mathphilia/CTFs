import re, socket, time

sock = socket.socket()
sock.connect(('this-is-not-lsb.seccon.games', 8080))
time.sleep(.2)

lines = sock.recv(1 << 16).decode().split('\n')
n = int(re.findall(r'\d+', lines[0])[0])
e = int(re.findall(r'\d+', lines[1])[0])
flag_bitlen = int(re.findall(r'\d+', lines[2])[0])
c = int(re.findall(r'\d+', lines[3])[0])

flag_bytelen = (flag_bitlen + 7) // 8
flag = b'SECCON{' + b'\x00' * (flag_bytelen - 7)
flag_int=int.from_bytes(flag, 'big')

for i in range((flag_bytelen - 7) * 8, 8 - 1, -1):
    print('\r' + flag.decode(), end = '')
    _flag_int = flag_int | (1 << i)
    mul = (1 << n.bit_length() - 2) // _flag_int
    send = c * pow(mul, e, n) % n
    sock.send(str(send).encode() + b'\n')
    if 'False' in sock.recv(1 << 16).decode():
        flag_int = _flag_int
    flag = flag_int.to_bytes(flag_bytelen, 'big')

print('\r' + flag.decode()[:-1] + '}')