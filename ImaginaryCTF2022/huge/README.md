# huge
category: Crypto
100 points, 137 solves

## 問題
> Huge primes = huge security

## 解法
素因数が大きかったらある程度の安全性は保証されるだろうが、$N$が大きいだけでは意味がない。$N$を試し割り法で素因数分解して
$$\varphi(p_1^{e_1}p_2^{e_2}\cdots p_k^{e_k})=\prod_{i=1}^kp_i^{e_i-1}(p_i-1)\quad(p_1,p_2,\dots,p_k:\text{ distinct primes})$$
により$\varphi(N)$を求め、あとは通常の手順と同様にして復号すればよい。
