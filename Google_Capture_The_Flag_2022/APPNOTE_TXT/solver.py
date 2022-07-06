with open('dump.zip', 'rb') as f:
    data = f.read()

fragments = {}
data_copy = data

while True:
    index = data_copy.find(b'PK', 4)
    if 0 < index:
        fragments[len(data) - len(data_copy)] = data_copy[:index]
        data_copy = data_copy[index:]
    else:
        fragments[len(data) - len(data_copy)] = data_copy
        break

flag=[]
for frag in fragments.values():
    if frag.startswith(b'PK\5\6'):
        index = int.from_bytes(frag[-6:-2], 'little')
        central_directory = fragments[index]
        len_filename = int.from_bytes(central_directory[28:32], 'little')
        filename = central_directory[-len_filename:]
        if not filename.startswith(b'flag'):
            continue
        flag.append(data[index-1])

print(bytes(flag))
