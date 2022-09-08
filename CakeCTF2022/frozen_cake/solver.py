with open('output.txt') as f:
    lines = f.readlines()

n = int(lines[0].split('=')[1])
a = int(lines[1].split('=')[1])
b = int(lines[2].split('=')[1])
c = int(lines[3].split('=')[1])

m = a * b * pow(c, -1, n) % n
flag = m.to_bytes((m.bit_length() + 7) // 8, 'big')
print(flag)
