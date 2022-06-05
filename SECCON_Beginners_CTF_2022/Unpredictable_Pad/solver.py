import re, socket, time
from predict import predict

def convert_base(n, base):
    #convert n to base `base`
    #convet_base(0b101000) -> [0, 0, 0, 1, 0, 1]
    ans = []
    while n:
        n, remainder = divmod(n, base)
        ans.append(remainder)
    return ans


sock = socket.socket()
sock.connect(('unpredictable-pad.quals.beginners.seccon.jp', 9777))

ipt = 1 - 2 ** (32 * 624)
assert ipt.bit_length() == 32 * 624
for _ in range(3):
    sock.send(str(ipt).encode() + b'\n')

time.sleep(1)
recv = sock.recv(1 << 16).decode()
lst = re.findall(r'The oracle is: -\d+', recv)
oracles = [int(i[len('The oracle is: '):]) for i in lst]
data = convert_base(oracles[2] ^ ipt, 1 << 32)
rand = predict(data)

enc = int(re.findall(r'Encrypted flag: \d+',recv)[0][len('Encrypted flag: '):])
length = enc.bit_length() + 1
length += -length % 8 - 1
flag = enc ^ rand.getrandbits(length)
print(flag.to_bytes((flag.bit_length() + 7) // 8, 'big'))
