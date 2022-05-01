enc = 'VEVASnm%gJ$ Jv%xx`"!"$c&h'

for key in range(32):
    print(bytes(c ^ key for c in enc.encode()))
