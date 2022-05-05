import re, socket, string, time

alpha = string.ascii_lowercase

def encrypt(msg, key):
    # written in main.py
    ret = ""
    i = 0
    for c in msg:
        if c in alpha:
            ret += alpha[alpha.index(c) + (alpha.index(key[i])) % len(alpha)] # msg + key
            i = (i + 1) % len(key)
        else:
            ret += c
    return ret

def decrypt(msg, key):
    ret = ""
    i = 0
    for c in msg:
        if c in alpha:
            ret += alpha[alpha.index(c) - (alpha.index(key[i])) % len(alpha)] # msg - key
            i = (i + 1) % len(key)
        else:
            ret += c
    return ret

sock = socket.socket()
sock.connect(('challs.actf.co', 31333))

for _ in range(50):
    time.sleep(.1)
    recv=sock.recv(1 << 16).decode()

    enc = re.findall(r'Challenge \d+: .+', recv)[0].split()[2]
    for i in range(len(enc) - 3):
        if re.match(r'[a-z]{4}\{.{10,50}\}', enc[i:]): # candidate for `actf{...}`
            key = decrypt(enc[i:i+4], 'actf') # key = enc - plain
            plain = decrypt(enc[i:], key) # plain = enc - key
            if plain[plain.index('}') + 1:][:4] == 'fleg':
                ans = plain[:plain.index('}')+1]
                sock.send(ans.encode() + b'\n')
                print(ans)
