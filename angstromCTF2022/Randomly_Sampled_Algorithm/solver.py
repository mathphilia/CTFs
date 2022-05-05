with open('output.txt') as f:
    output = f.readlines()

n = int(output[0].split()[-1])
e = int(output[1].split()[-1])
c = int(output[2].split()[-1])
phi = int(output[3].split()[-1])

d = pow(e, -1, phi)
m = pow(c, d, n)

print(m.to_bytes((m.bit_length() + 7) // 8, 'big'))
