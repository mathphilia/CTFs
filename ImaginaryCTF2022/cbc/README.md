# cbc
category: Crypto
100 points, 123 solves

## 問題
> I don't trust everyone's CBC implementations. So I rolled my own, with A HUNDRED PERCENT GUARANTEE OF DATA INTEGRITY!

## 解法
CBCモードのAESの問題…と思いきや、あからさまに実装にミスがある。第2ブロック以降の鍵と暗号文が丸見えなので簡単に復号できる。また、平文がflagの繰り返しになっているので第1ブロックが復号できないことには問題ない。
