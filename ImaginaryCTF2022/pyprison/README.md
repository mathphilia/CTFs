# pyprison
category: Misc
100 points, 180 solves

## 問題
> What's a CTF without a good, old-fashioned pyjail?  
>   
> `nc pyprison.chal.imaginaryctf.org 1337`

## 解法
"()abcdefghijklmnopqrstuvwxyz"のみで構成された文字列をexecしてもらえる。`()`が使えるのだからinput函数を使おう。ついでに

```py
exec(input())
while True:exec(input())
```

とすれば任意の1行コマンドを連続で実行してもらえる。あとは`os.system`函数なり`subprocess.run`函数なりを使えばファイルを読み出せる。
