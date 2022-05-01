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
$_=k$の処理の終了時の$a,b,\text{text}$の値をそれぞれ$a_k,b_k,\text{text}_k$とおく。xorの可換性、結合性、そして$a\text^a=0$から、
$$\text{text}_0=a_0\text^((b_0\text^\text{message})\text^a_0)\text^b_0\text^a_0=\text{message}\text^(a_0\text^a_0\text^a_0\text^b_0\text^b_0)=\text{message}\text^a_0$$
$$\text{text}_1=\text{text}_0\text^a_1=(\text{message}\text^a_0)\text^a_1=\text{message}\text^(a_0\text^a_1)$$
$$\text{text}_{99}=\text{message}\text^(a_0\text^a_1\text^\cdots\text^a_{99})$$
よって、最終的に出てくる暗号文は平文と0以上32未満の整数とのxorに過ぎないことが分かる。よって32通りの全探索でflagが求まる。
