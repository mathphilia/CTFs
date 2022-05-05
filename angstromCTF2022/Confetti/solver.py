with open('confetti.png', 'rb') as f:
    data = f.read()

magic_number = b'\x89PNG\r\n\x1a\n'
lst = data.split(magic_number)

for i in range(1, len(lst)):
    with open(f'flag{i}.png', 'wb') as f:
        f.write(magic_number + lst[i])
