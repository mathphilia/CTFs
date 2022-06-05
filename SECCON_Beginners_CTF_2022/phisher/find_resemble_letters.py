import unicodedata

for i in range(10000):
    try:
        c = chr(i)
        s = unicodedata.name(c)
        if 'LATIN SMALL LETTER M' in s:
            print(i, c, s)
    except ValueError:
        pass
