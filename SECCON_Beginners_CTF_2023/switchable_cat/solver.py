from numpy import matrix


class LFSR:
    def __init__(self):
        self.bits = 128
        self.rr = seed
        self.switch = 0
    def next(self):
        r = self.rr
        if self.switch == 0:
            b = ((r >> 0) & 1) ^ \
                ((r >> 2) & 1) ^ \
                ((r >> 4) & 1) ^ \
                ((r >> 6) & 1) ^ \
                ((r >> 9) & 1)
        if self.switch == 1:
            b = ((r >> 1) & 1) ^ \
                ((r >> 5) & 1) ^ \
                ((r >> 7) & 1) ^ \
                ((r >> 8) & 1)
        r = (r >> 1) + (b << (self.bits - 1))
        self.rr = r
        self.switch = 1 - self.switch
        return r & 1
    
    def gen_randbits(self, bits):
        key = 0
        for i in range(bits):
            key <<= 1
            key += self.next()
        return key


def power_mod2(mat, n):
    # n-th power of mat (mod 2)
    power = mat ** 0
    tmp = mat ** 1
    while n:
        if n & 1:
            power *= tmp
        tmp = tmp ** 2 % 2
        n //= 2
    return power % 2


def proceed(register, steps):
    rr = register.rr
    state = matrix([[int(bit)] for bit in f'{rr:0128b}'])
    A = [[0] * 118 + [1, 0, 0, 1, 0, 1, 0, 1, 0, 1]]
    A += [[i == j for j in range(128)] for i in range(127)]
    A = matrix(A)
    B = [[0] * 118 + [0, 1, 1, 0, 1, 0, 0, 0, 1, 0]]
    B += [[i == j for j in range(128)] for i in range(127)]
    B = matrix(B)
    state = power_mod2(B * A, steps // 2) * state
    if steps & 1:
        state = A * state
        register.switch = 1
    state %= 2
    register.rr = int(''.join(str(int(bit)) for bit in state), 2)


seed = 219857298424504813337494024829602082766
cipher = 38366804914662571886103192955255674055487701488717997084670307464411166461113108822142059
lfsr = LFSR()

cat = ord("🐈") * ord("🐈") * ord("🐈")
proceed(lfsr, cat * 8)

length = (cipher.bit_length() + 7) // 8
key = lfsr.gen_randbits(length * 8)
flag = cipher ^ key

print(flag.to_bytes((flag.bit_length() + 7) // 8, 'big'))