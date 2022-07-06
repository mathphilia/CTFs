# Welcome
category: Crypto
201 points, 50 solves

## 問題
> It is well known that any RSA encryption can be undone by just encrypting the ciphertext over and over again.
> If the RSA modulus has been chosen badly then the number of encryptions necessary to undo an encryption is small.
> However, if the modulus is well chosen then a cycle attack can take much longer. This property can be used for a timed release of a message.
> We have confirmed that it takes a whopping 2^1025-3 encryptions to decrypt the flag.
Pack out your quantum computer and perform 2^1025-3 encryptions to solve this challenge. Good luck doing this in 48h.

## 解法
**注意: この解法は相当時間がかかるため、正規の方法でない恐れがあります。**  
また、Markdownが異常に読みにくくなっているので[原文](https://raw.githubusercontent.com/mathphilia/CTFs/main/Google_Capture_The_Flag_2022/CYCLING/README.md)を読んでください。  
It is well knownとか言われても知らないので証明してみる。問題文で述べられている定理を整理すると以下のようになる。  

> **定理1.**(不完全版) 一部の例外(後述)を除く任意の$2$以上の自然数$n,e$に対し、以下が成り立つ。暗号化函数$\operatorname{encrypt}:\mathbb Z_n^*\to\mathbb Z_n^*$を
> $$\operatorname{encrypt}(m)=m^e\mod n$$
> $$\operatorname{encrypt}^a=\underbrace{\operatorname{encrypt}\circ\operatorname{encrypt}\circ\dots\circ\operatorname{encrypt}}_{a\text{ times composition}}$$
> で定め、任意の平文$m\in\mathbb Z_n^*$に対して暗号文$c=\operatorname{encrypt}(m)$を考えるとき、ある非負整数kが存在して
> $$\operatorname{encrypt}^k(c)=m$$
> が成り立つ。

最後の式は指数法則を用いて$c^{e^k}\mod n=m^{e^{k+1}}\mod n=m$と変形でき、$m$がmod $n$で乗法逆元を持つことから$m^{e^{k+1}-1}\mod n=1$と書き直せる。ここで、"well-knownな"2つの定理を述べる。

> **定理2.(Carmichaelの定理)** Carmichel函数$\lambda:\mathbb N_{\geqq2}\to\mathbb N$を以下のように再帰的に定義する。  
> $n$が素数$p$と正整数$s$を用いて$n=p^s$と書けるとき、
> $$\lambda(n)=\begin{cases}2^{s-2}&(p=2\text{ and }3\leqq s)\\p^{s-1}(p-1)&(\text{otherwise})\end{cases}$$
> $n$が$i$個($i\in\mathbb N_{\geqq2}$)の素数$p_1,p_2,\dots,p_i$と正整数$s_1,s_2,\dots,s_i$を用いて$n=p_1^{s_1}p_2^{s_2}\cdots p_i^{s_i}$と書けるとき、
> $$\lambda(n)=\operatorname{LCM}\Big(\lambda(p_1^{s_1}),\lambda(p_2^{s_2}),\dots,\lambda(p_i^{s_i})\Big)$$
> なお、素因数分解の一意性からこの定義はwell-definedである。このとき、Carmichael函数は以下を満たす正整数$k$の最小値になっている。
> $$\text{任意の}m\in Z_n^*\text{に対して}m^k\mod n=1$$

面倒なので証明略。

> **定理3.** $b$を$2$以上の自然数とする。$b$と互いに素な任意の$n\in\mathbb N_{\geqq2}$に対して、$b$進repunit数であって$n$の倍数であるものが存在する。$b$進repunit数とは、$b$進整数で書いたとき全ての桁が1になる自然数、即ち正整数mを用いて$1+b+b^2+\dots+b^{m-1}$と書ける数のことである。  
> **証明)** $b$進$m$桁のrepunit数を$R_{b,m}$とおく。$b$と$n$が互いに素であることから$R_{b,1},R_{b,2},R_{b,3},\dots,R_{b,n}$割った余りはいずれも$0$ではない、つまり$1,2,3,\dots,n-1$のどれかである。鳩の素原理からこれら$n$個のなかに$n$で割った余りが一致するような$R_{b,i},R_{b,j}\;(i>j)$が存在する。この$i,j$に対して$R_{b,i}-R_{b,j}$は$n$の倍数になる。
> $$R_{b,i}-R_{b,j}=b^i+b^{i-1}+b^{i-2}+\dots+b^j=(b^{i-j}+b^{i-j-1}+b^{i-j-2}+\dots+1)b^j=R_{b,i-j}b^j$$
> であり、$b^j$は$n$と互いに素であるので$R_{b,i-j}$は$n$の倍数。

以上のことから**定理1.**の完全版とその証明を述べる。

> **定理1.**(完全版) 任意の$2$以上の自然数$n,e$に対し、$\lambda(n)$と$e$が互いに素であるとき以下が成り立つ。暗号化函数$\operatorname{encrypt}:\mathbb Z_n^*\to\mathbb Z_n^*$を
> $$\operatorname{encrypt}(m)=m^e\mod n$$
> $$\operatorname{encrypt}^a=\underbrace{\operatorname{encrypt}\circ\operatorname{encrypt}\circ\dots\circ\operatorname{encrypt}}_{a\text{ times composition}}$$
> で定めるとき、ある非負整数kが存在して
> $$m^{e^{k+1}-1}\mod n=1$$
> が成り立つ。  
> **証明)** **定理3.**より$e^{k+1}-1=R_{e,k+1}$が$\lambda(n)$の倍数となるような非負整数$k$が存在する。この$k$に対して$\lambda(n)r=e^{k+1}-1$として正整数$r$を定める。このとき**定理2.**から
> $$m^{e^{k+1}-1}\mod n=(m^{\lambda(n)})^r\mod n=1$$
> が分かる。以上で示された。

さて、**定理1.**から$m^{e^{k+1}-1}\mod n=1$なる$k$が存在することは分かったが、それがいくつになるのか、もっと言えばこの等式を満たす非負整数$k$の最小値$k_\min$がいくつであるのかはこの定理からは分からない。$m^{e^{k+1}-1}\mod n=1$になるのは$e^{k+1}-1$が$\lambda(n)$の倍数であるときだが、これは言い換えれば$e^{k+1}\mod\lambda(n)=1$となるときである。Carmichaelの定理から$k+1=\lambda(\lambda(n))$のとき$e^{k+1}\mod\lambda(n)=1$となる。$e^{k+1}\mod\lambda(n)=1$であることと$k+1$が$k_\min$の倍数であることは同値なので、$k_\min$は$\lambda(\lambda(n))$の約数となる。  
ここまでわかれば後は計算するのみ。$\lambda(n)$の倍数となる数が得られれば通常の手順で復号できるので、これを目標にする。今回の問題では$k_\min=2^{1025}-3$であったから$\lambda(\lambda(n))$は$2^{1025}-2$の倍数であり、更に言えば$\lambda(\lambda(n))=2^{1025}-2$であることが期待される(そこそこの割合の$n$で成り立つはず)。$\lambda(n)=p_1^{s_1}p_2^{s_2}p_3^{s_3}\cdots p_i^{s_i}$としたとき、十分大きい$p$に対応する$s$は$1$になりそうである。$\lambda(\lambda(n))=2^{1025}-2$ということは$p_1-1,p_2-1,p_3-1,\dots,p_i-1$が$2^{1025}-2$の約数ということになる。以上のことから、$2^{1025}-2$の約数全体を$d_1,d_2,d_3,\dots,d_l$として
$L=\operatorname{LCM}(d_1,d_2,d_3,\dots,d_l)$
とおけば$L$が$\lambda(n)$の倍数となるように思う。確証はないが実際上手くいったのでヨシ!
