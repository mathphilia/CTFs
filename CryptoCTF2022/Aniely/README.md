# Aniely
category: Crypto
66 points, 76 solves

## 問題
> There is stream cipher, try to keep it smooth!

## 解法
函数`aniely_stream`をfとおく。key=flag xor passphraseと2bytes乱数randに対して、enc=passphrase xor f(key) xor rand\*8である。keyが与えられているので、enc xor key xor f(key)を計算することによりflag xor rand\*8を得る。flagの先頭2bytesはb'CC'であるはずなので、randの値も分かる。以上から(flag xor rand\*8) xor rand\*8を計算することによりflagが得られる。また、randは2bytesなので全探索することもできる。以下は別解である。

```py
#函数等はsolver.pyと同様に定義
for r in range(256 ** 2):
    rand = r.to_bytes(2, 'big')
    passphrase = aniely_decrypt(enc, key, rand)
    flag = bytes(a ^ b for a, b in zip(passphrase, key))
    if flag.startswith(b'CC'):
        print(flag)
```
