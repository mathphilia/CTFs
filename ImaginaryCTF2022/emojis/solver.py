with open('emojis.txt') as f:
    enc = f.read()

flag_bin = enc.replace('👍', '1').replace('👎', '0')
flag = bytes(int(flag_bin[i:i + 8], 2) for i in range(0, len(flag_bin), 8))
print(flag)
