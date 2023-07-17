# Elliptic Ring RSA
category: Crypto
178 points, 27 solves

## 問題
> RSA is hard over integer ring.  
> What about RSA over elliptic curve ring (!?)

## 解法
$K=\mathbb F_p$ とし、 $K$ 上の楕円曲線群 $\{(x,y)\mid y^2=x^3+ax+b\}$ を $E$ とする。このとき環`EllipticRing`は群環 $KE$ と同型である。環 $\mathbb Z/n\mathbb Z$ 上の(つまりは"普通の")RSA暗号の復号の仕組みを振り返ると、 $\varphi(n)=|(\mathbb Z/n\mathbb Z)^\times|$ として平文 $m\in(\mathbb Z/n\mathbb Z)^\times$ に対して $(m^e)^{e^{-1}\;\bmod\;\varphi(n)}=m$ が成り立つことを使っているのであった。今回は $KE$ 上のRSA(?)暗号であるが、同様の方法で復号できる。即ち、 $\varphi=|KE^\times|$ とおくと平文 $m\in KE^\times$ に対して $(m^e)^{e^{-1}\;\bmod\;\varphi}=m$ が成り立つ。ソースコードで $m\in KE^\times$ は保証されていないが、後述のことから分かるように $KE$ の元はほぼ $KE^\times$ に入っているので問題ない。  
それでは以下で $\varphi=|KE^\times|$ を求めていく。 $E$ は生成元 $g$ を持つ(証明は分からないがSageMathに生成元を求めるメソッドがある)ので巡回群であり、したがって $n=|E|$ (この値はSageMathで求まる)とすれば $\mathbb Z/n\mathbb Z$ と同型である。更に、このとき $KE\cong K[X]/(X^n-1)$ が言える。実際、以下の写像は環同型である。  
$$\psi:KE\to K[X]/(X^n-1),\sum_{k=0}^{n-1}a_kg^k\mapsto\sum_{k=1}a_kX^k$$
ただし、 $a_k\in K$ とする。 $K[X]/(X^n-1)$ の乗法群は $\{f+(X^n-1)\in K[X]/(X^n-1)\mid\gcd(f,X^n-1)=1\}$ であるから、 $K$ 係数で次数 $n$ 未満の多項式(零多項式を含む)のうち $X^n-1$ と互いに素であるものの個数を数えればよい。 $X^n-1$ を $K[X]$ 上因数分解したものを $f_1(X)^{e_1}f_2(X)^{e_2}f_3(X)^{e_3}\dots f_k(X)^{e_k}$ とおくと、 $f\in K[X]$ について  
$$\gcd(f,X^n-1)\neq1\iff f\in\bigcup_{k=1}^n(f_k(X))$$
が成り立つ。 $K[X]/(X^n-1)$ において $X^n-1$ の $r$ 次の約数で生成されるイデアルの濃度は $p^{n-r}$ と求まるから、包除原理を使えば $K[X]/(X^n-1)$ の乗法群の位数が求まる。ただし $X^n-1$ の因数は多いので、ナイーヴに実装すると時間がかかりすぎる。したがって因数の次数ごとにまとめて計算するとよい。以下、 $d=e^{-1}\bmod|KE|$ とおく。  
ここまでの議論から暗号文 $C$ に対して $C^d$ を計算すれば平文が得られると分かるが、`ER.pow`は繰り返し二乗法を使っている割に遅く、 $13$ 乗ですら数十秒かかる。 $d\fallingdotseq\varphi\fallingdotseq p^n$ で $p=211,n=192$ なので`ER.pow`では箸にも棒にもかからない。ではどうするか。ここでも $KE\cong K[X]/(X^n-1)$ であることを使う。即ち前述の $\psi$ を用いて $\psi^{-1}(\psi(C)^d)$ を求めることにより $C^d$ を計算する。多項式の乗算および剰余算はそれなりに速く行えるので十分高速にflagが求まる。
