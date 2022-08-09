# Secure Encoding: Hex
category: Crypto
100 points, 195 solves

## 問題
> Cryptograms == encryption, right? Flag is readable English.

## 解法
flagを16進数で表したうえで、単表換字式暗号により暗号化している。flagが`ictf{`から始まり`}`で終わること、`_`がそこそこの頻度で出現すること、`ictf{　}`の中身はある程度意味のある英文になっていることなどから換字の対応表を埋めていく。結果的に得られる対応表は以下の通り(4, 5, aは暗号文に登場しない)。

```
0123456789abcdef
6712  de4c 359bf
```
