# I don't know why, but I can't get a flag about once every two times.
import socket, time

sock = socket.socket()
sock.connect(('challs.actf.co', 31223))

time.sleep(.3)
recv = sock.recv(1 << 16)
print(recv.decode(errors = 'replace'))
sock.send(b'-' * 48)

time.sleep(.3)
recv = sock.recv(1 << 16)
print(recv.decode(errors = 'replace'))
start = 'Nice to meet you, ------------------------------------------------'
end = '!\nGuess my name and you\'ll get a flag!\n'
sock.send(recv[len(start):-len(end)] + b'\n')

time.sleep(.3)
recv = sock.recv(1 << 16)
print(recv.decode(errors = 'replace'))
