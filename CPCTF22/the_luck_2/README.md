# the luck 2
category: Misc
344.19 points, 15 solves

## 問題
> `nc theluck2.cpctf.space 30001`
> the luck 1とthe luck 2は独立した問題です。

## 解法
`random.getrandbits(32)`の値を際限なく教えてもらえるので、[Mersenne Twisterの出力を推測してみる - ももいろテクノロジー](https://inaz2.hatenablog.com/entry/2016/03/07/194147)を参考にして次の値を予測する。
