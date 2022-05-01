import socket, subprocess, time

sock = socket.socket()
sock.connect(('theluck1.cpctf.space', 30002))

now = str(time.time()).encode()
PIPE = subprocess.PIPE
out, err = subprocess.Popen(['gcc', 'solver.c']).communicate()
out, err = subprocess.Popen(['./a.out'], stdin = PIPE, stdout = PIPE, stderr = PIPE).communicate(input = now)

sock.send(out + b'\n')
time.sleep(.5)
print(sock.recv(1 << 16).decode())
