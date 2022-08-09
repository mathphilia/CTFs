from requests import get, post
from string import ascii_uppercase

res = get('http://03.cr.yp.toc.tf:11117/flag/fetch')
enc_flag = res.json()['flag'].replace(' ', '')[10:-10]
url = 'http://03.cr.yp.toc.tf:11117/m209/encipher'

plain = ''
for i in range(len(enc_flag)):
    for c in ascii_uppercase[::-1]:
        _plain = plain + c
        res = post(url, {'plain': _plain})
        enc = res.json()['cipher'].replace(' ', '')[10:-10]
        print('\r' + _plain.replace('Z', ' '), end = '')
        if enc[:i + 1] == enc_flag[:i + 1]:
            plain += c
            break

print()
