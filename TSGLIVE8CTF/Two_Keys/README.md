# Two Keys
category: Crypto
250 points, 5 solves

## 問題
> フラグを二つに分けて、別々の公開鍵で暗号化しました

## 解法
2つの公開鍵N, N'は、N=p×q (p, q: 素数)とするとN'=(pの次の素数)×(qの次の素数)という形になっている。ここで、pの次の素数をp+δ<sub>p</sub>, qの次の素数をq+δ<sub>q</sub>とする。δ<sub>p</sub>とδ<sub>q</sub>の値を決めると、未知数が2つ(pとq)で方程式が2本(N=…とN'=…)なので以下のようにしてp, qを求めることができる。  
<div align="center"><img src="https://github.com/mathphilia/CTFs/blob/main/images/TSGLIVE8CTF/Two_Keys_1.png?raw=true"></div>  
ではδ<sub>p</sub>とδ<sub>q</sub>をどう求めるのかというと、これは2, 4, 6, …と全探索すればよい。512bitでも素数の密度というのはそれほど小さいいものではなく、素数定理によれば512bit素数の間隔は平均(?)して約354である。なので、2～1000くらいの範囲を調べれば見つかるだろうとたかをくくり計算する。
