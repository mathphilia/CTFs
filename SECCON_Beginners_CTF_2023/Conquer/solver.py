def LOR(bits, N):
    for _ in range(N):
        bits = (bits >> 1) | ((bits & 1) << (length - 1))
    return bits


diff = 0
while True:
    key = 364765105385226228888267246885507128079813677318333502635464281930855331056070734926401965510936356014326979260977790597194503012948
    cipher = 92499232109251162138344223189844914420326826743556872876639400853892198641955596900058352490329330224967987380962193017044830636379
    length = cipher.bit_length() + diff

    for i in range(32):
        cipher ^= key
        key = LOR(key, pow(cipher, 3, length))

    flag = cipher ^ key
    flag = flag.to_bytes((flag.bit_length() + 7) // 8, 'big')
    if flag.startswith(b'ctf4b{'):
        print(flag)
        break
    else:
        diff += 1