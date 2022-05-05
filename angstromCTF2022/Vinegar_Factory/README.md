# Vinegar Factory
category: Crypto  
100 points, 238 solves

## 問題
> Clam managed to get parole for his dumb cryptography jokes, but after making yet another dumb joke on his way out of the courtroom, he was sent straight back in. This time, he was sentenced to 5 years of making dumb Vigenere challenges. Clam, fed up with the monotony of challenge writing, made a program to do it for him. Can you solve enough challenges to get the flag?
> 
> Connect to the challenge at `nc challs.actf.co 31333`. [Source](main.py)

# 解法
50問連続でVigenére暗号を解かなくてはならない。鍵は4文字であり、平文はすべて

```
(2000文字以下)actf{(10~50文字)}fleg(2000文字以下)
```

の形をしている。なお、`actf{　}`の内側は英小文字と`_`で、冒頭及び末尾の`(2000文字以下)`の部分はそれに加えて`{}`で構成されており、`fleg`は誤字ではない。条件より平文のどこかに`actf`があることが分かるので、その位置を全探索して鍵を計算し、`fleg`の有無で正しいかチェックする。
