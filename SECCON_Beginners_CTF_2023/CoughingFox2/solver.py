cipher = [4396, 22819, 47998, 47995, 40007, 9235, 21625, 25006, 4397, 51534, 46680, 44129, 38055, 18513, 24368, 38451, 46240, 20758, 37257, 40830, 25293, 38845, 22503, 44535, 22210, 39632, 38046, 43687, 48413, 47525, 23718, 51567, 23115, 42461, 26272, 28933, 23726, 48845, 21924, 46225, 20488, 27579, 21636]

plain = b'c'
for i in range(len(cipher)):
    for c in cipher:
        sqrt = (c - i) ** 0.5
        if int(sqrt) == sqrt:
            plain += bytes([int(sqrt) - plain[-1]])
            cipher.remove(c)
            break

print(plain)