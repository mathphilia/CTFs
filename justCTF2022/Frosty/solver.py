import re, socket, time

import json, hashlib
from fastecdsa.curve import P192 as Curve
from fastecdsa.point import Point
from secrets import randbits

import subprocess

N = Curve.q.bit_length()

def mod_hash(msg : bytes, R : Point) -> int:
    h = hashlib.sha256()
    h.update(len(msg).to_bytes(64, 'big'))
    h.update(msg)
    h.update(R.x.to_bytes(N//8, 'big'))
    h.update(R.y.to_bytes(N//8, 'big'))
    return int(h.hexdigest(), 16) % Curve.q

def verify(pubkey : Point, m : bytes, z : int, c : int) -> bool:
    R = z*Curve.G - c * pubkey
    return c == mod_hash(m, R)

def coords(p : Point) -> (str, str):
    return (hex(p.x)[2:], hex(p.y)[2:])


m = b'Gimme!'
pubkey = Curve.G
R = Curve.G
c = mod_hash(m, R)
z = (c + 1) % Curve.q
assert verify(pubkey, m, z, c)

sock = socket.socket()
sock.connect(('frosty.nc.jctf.pro', 4444))

time.sleep(1)
recv = sock.recv(1 << 16).decode()
command = re.findall(r'hashcash -mb26 .+', recv)[0]
out, err = subprocess.Popen(command.split(), stdout = -1).communicate()
sock.send(out)

sock.send(json.dumps(
    {'op': 'verify', 'm': m.hex(), 'z': hex(z)[2:], 'c': hex(c)[2:], 'pubkey': coords(pubkey)}
    ).encode() + b'\n')
time.sleep(1)
recv = sock.recv(1 << 16).decode()
print(recv)
