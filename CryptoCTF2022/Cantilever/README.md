# Cantilever
category: Crypto
79 points, 60 solves

## 問題
> What if you can find the message? If you can, that means you are genius, because we harden our crypto system with a very modern tool!

## 解法
RSA暗号と離散対数問題である。$p-1,q-1$の素因数がすべて$19$bit以下であることから$n$は$p-1$法により素因数分解できる。$\bmod$素数の離散対数問題は、法$-1$が小さい素数の積であればPohlig-Hellman法によって比較的簡単に解くことができる。[solver.py](CryptoCTF2022/Cantilever/solver.py)ではbaby-step giant-step法とPohlig-Hellman法を使って求めたが、[Discrete logarithm calculator](https://www.alpertron.com.ar/DILOG.HTM)を使えば簡単に求めることができる。また、$\bmod q$ ($q$はsolver.pyにおける値)での$65537$の位数$\operatorname{ord}_q(65537)$が$q-1$でないためsolver.pyの方法そのままで計算すると$m_2$が求まらない。$p$の場合と同様に離散対数を求めた上で$\operatorname{ord}_q(65537)$で割った余りを計算すれば$m_2$が求まる。なお、$m_2$が$p,q$ ($2048$bit=$256$bytes)に比べて十分小さいため$\bmod p$での離散対数問題だけ解けば十分である。
