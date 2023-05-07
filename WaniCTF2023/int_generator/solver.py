import chall

with open('output.txt') as f:
    enc1 = int(f.readline().split(':')[1])
    enc2 = int(f.readline().split(':')[1])
    enc3 = int(f.readline().split(':')[1])

for flag in range(0, 2 ** 35 + 1, 2 ** 18):
    enc = chall.int_generator(flag)
    if enc == enc1:
        flag1 = flag
    elif enc == enc2:
        flag2 = flag
    elif enc == enc3:
        flag3 = flag

print('-'*50)
print('FLAG{%d_%d_%d}' % (flag1, flag2, flag3))