from Crypto.Cipher import AES


p = 4170887899225220949299992515778389605737976266979828742347
ct = bytes.fromhex("ae7d2e82a804a5a2dcbc5d5622c94b3e14f8c5a752a51326e42cda6d8efa4696")
q = 9213409941746658353293481

power = pow(7, 444780066250058017668829040430952, p)
tmp = pow(7, (p - 1) // q, p)

for key in range(444780066250058017668829040430952, 1 << 128, (p - 1) // q):
    if power == 0x49545b7d5204bd639e299bc265ca987fb4b949c461b33759:
        break
    power = power * tmp % p

key = key.to_bytes((key.bit_length() + 7) // 8, 'big')
print(AES.new(key, AES.MODE_ECB).decrypt(ct))