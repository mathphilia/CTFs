import re, socket, time

sock = socket.socket()
sock.connect(('otp.chal.imaginaryctf.org', 1337))
sock.send(b'FLAG\n' * 100)

time.sleep(1)
recv = sock.recv(1 << 16).decode()

result = re.findall('Encrypted flag: [0-9a-f]+', recv)
result = [s[len('Encrypted flag: '):] for s in result]
result = [bytes.fromhex(s) for s in result]
result = [''.join(f'{i:08b}' for i in data) for data in result]

flag = ''
for idx in range(len(result[0])):
    zero, one = 0, 0
    for data in result:
        if data[idx] == '0':
            zero += 1
        else:
            one += 1
    if zero < one:
        flag += '0'
    else:
        flag += '1'

flag = int(flag, 2)
flag = flag.to_bytes((flag.bit_length() + 7) // 8, 'big')
print(flag)
