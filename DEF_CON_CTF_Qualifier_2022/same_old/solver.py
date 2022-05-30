import binascii, itertools

def crc32_reverse(data, crc):
    _crc = crc
    crc ^= 0xffffffff
    for byte in data[::-1]:
        for _ in range(8):
            if crc.bit_length() < 32:
                crc <<= 1
            else:
                crc = ((crc ^ 0xEDB88320) << 1) + 1
        crc ^= byte
    ans = crc ^ 0xffffffff
    assert binascii.crc32(data, ans) == _crc
    return ans

def crc32_falsify(initial, target):
    crc_initial = binascii.crc32(initial)
    crc_target = binascii.crc32(target)
    tail = crc32_reverse(crc_initial.to_bytes(4, 'little'), crc_target)
    ans = initial + tail.to_bytes(4, 'little')
    assert binascii.crc32(ans) == binascii.crc32(target)
    return ans
    

alphanum = list(range(48, 58)) + list(range(65,91)) + list(range(97,123))
team_name = b'TEAM_NAME' # YOUR TEAM NAME

for add in itertools.product(alphanum, repeat=2):
    initial = team_name + bytes(add)
    flag = crc32_falsify(initial, b'the')
    if all(i in alphanum for i in flag[len(team_name):]):
        print(flag)
        break
