# xxorxx
category: Crypto  
190.35 points, 36 solves

## 問題
> たくさん書き換えれば誰にもわからないよね！
> 
> 暗号
> ```
> VEVASnm%gJ$ Jv%xx`"!"$c&h
> ```
> ソースコード
> ```py
> import random
> from secret import FLAG
> 
> def encrypt(message):
>     text = list(message.encode('ascii'))
>     for _ in range(100):
>         a = random.randrange(1, 32)
>         b = random.randrange(1, 32)
>         for i in range(len(text)):
>             text[i] = a ^ ((b ^ text[i]) ^ a) ^ b ^ a
>     ciphertext = bytes(text)
>     return ciphertext
> 
> cipher = encrypt(FLAG)
> with open('ciphertext', 'wb') as f:
>     f.write(cipher)
> ```

## 解法
\_=kの処理の終了時のa, b, textの値をそれぞれa<sub>k</sub>, b<sub>k</sub>, text<sub>k</sub>とおく。xorの可換性、結合性、そしてa^a=0から、  
![数式1](GitHub/CTFs/images/CPCTF22/xxorxx_1.png)
よって、最終的に出てくる暗号文は平文と0以上32未満の整数とのxorに過ぎないことが分かる。よって32通りの全探索でflagが求まる。
