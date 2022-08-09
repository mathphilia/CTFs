# Infinity castle
category: Crypto
131 points, 32 solves

## 問題
> Can you break our new schema and decrypt the mixed encrypted message without having the public key and shared secret?!

## 解法
ソースコードを見ると、  
> If you run these 3 functions (diamond, triage, summarize) with big numbers, they will never end You need to optimize them first

とある。`diamond`, `triage`, `summarize`の3つの函数を現実的な時間で処理することができれば復号できそうである。まず、`diamond`について、
$$\operatorname{diamond}(n)=\sum_{i=0}^{n-1}(2i+1)=n^2$$
となる。また、`triage`について、各forループの開始時点の`index`の値を$\text{index}_i$とすると
$$\text{index}_0=0,\;\text{index}_i=\sum_{k=0}^{i-1}k=\frac12i(i-1)\;(1\leqq i)$$
$$\therefore\text{index}_i=\frac12i(i-1)\;(0\leqq i)$$
$$\operatorname{triage}(n)=\sum_{i=0}^{n-1}\{6(i+\text{index}_i)+1\}=\sum_{i=0}^{n-1}(3i^2+3i+1)=\sum_{i=0}^{n-1}\{(i+1)^3-i^3\}=n^3$$
最後に、`summarize`について考える。TaylorSeries.coefficient(n)の出力を$\operatorname{coef}(n)$とすると
$$\operatorname{coef}(n)=\prod_{i=1}^n\frac1i\left(\frac12-i+1\right)$$
$$\operatorname{coef}(0)=1,\;\operatorname{coef}(1)=\frac12,\;\operatorname{coef}(2)=-\frac18,\;\operatorname{coef}(3)=\frac1{16},\;\ldots$$
よって、TaylorSeries.find(x)の出力を$f(x)$とすると
$$f(x)=\sum_{i=0}^{\text{order}-1}\operatorname{coef}(i)(x-1)^{\frac12-i}=(x-1)^\frac12+\frac12(x-1)^{-\frac12}-\frac18(x-1)^{-\frac32}+\frac1{16}(x-1)^{-\frac52}+\cdots$$
となる。グラフを考えると$\operatorname{summarize}(b)\fallingdotseq\displaystyle\int_2^bf(x)dx$であることが分かるから、
\begin{align*}
\operatorname{summarize}(b)&\fallingdotseq\int_2^b\left\{(x-1)^\frac12+\frac12(x-1)^{-\frac12}-\frac18(x-1)^{-\frac32}+\frac1{16}(x-1)^{-\frac52}\cdots\right\}dx\\
&=\left[\frac23(x-1)^\frac32+(x-1)^\frac12+\frac14(x-1)^{-\frac12}-\frac1{24}(x-1)^{-\frac32}+\cdots\right]_2^b\\
&=\left\{\frac23(b-1)^\frac32+(b-1)^\frac12+\frac14(b-1)^{-\frac12}-\frac1{24}(b-1)^{-\frac32}+\cdots\right\}-\left(\frac32+\frac12+\frac14-\frac1{24}+\cdots\right)\\
&\fallingdotseq\frac23(b-1)^\frac32+(b-1)^\frac12
\end{align*}
ただし、最後の$\fallingdotseq$では$b$が十分大きい場合を考えた。padded\_msgの下位bitは乱数であるから、$\operatorname{summarize}(b)$の値は上位bitだけ分かればよい。従って`summarize`は多少雑な評価でも問題ない。以上で3つの函数の出力を求める方法が分かったので復号する。$c_0=|p^2-q^2|,\;c_1=p^3+3n(p+q)+q^3=(p+q)^3$なので、$P=\max\{p,q\},Q=\min\{p,q\}$とすると$\sqrt[3]{c_1}=P+Q,\;P-Q=\dfrac{P^2-Q^2}{P+Q}=\dfrac{c_0}{\sqrt[3]{c_1}}$である。よって$P=\dfrac12\left(\sqrt[3]{c_1}+\frac{c_0}{\sqrt[3]{c_1}}\right),\;Q=\dfrac12\left(\sqrt[3]{c_1}-\frac{c_0}{\sqrt[3]{c_1}}\right)$である。ここから$n=pq=PQ$が求まる。$n,P,Q,e,\text{enc}_1$が分かっているから$\text{enc}_0$が分かり、$n$からxor\_keyが求まるのでflagが得られる。
