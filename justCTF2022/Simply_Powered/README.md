# Welcome
category: Crypto
260 points, 29 solves

## 問題
> Just calculate root. :)
> ```
> # Use only one server:
> nc simply-powered-ams3.nc.jctf.pro 4444 #  142.93.236.95
> nc simply-powered-nyc3.nc.jctf.pro 4444 #  159.203.115.238
> nc simply-powered-sgp1.nc.jctf.pro 4444 # 167.172.66.141
> ```

## 解法
[こちらのサイト](https://maspypy.com/数学-n乗の計算#toc10)を参考にしていろいろ試行錯誤すると、$\mathbb F_p$上の行列$A$に対してある$n\geqq2$が存在し、$A^{p^n}=A^p$となるようだと気づく。つまりこの$n$に対して列$A^1,A^2,A^3,\ldots$の周期の1つが$p^n-p$となる(なお、$A$が正則でない場合は周期が初項から始まらないこともあり得るがそれほど確率が高くなさそうなので無視)。よって、与えられた行列を$M$, modulusを$p$, 指数を$e$とすると、ある自然数$n,k$が存在して
$$(M^{e^{-1}\%p^n-p})^e=M^{k(p^n-p)+1}=M^{(k-1)(p^n-p)+1}=M^{(k-2)(p^n-p)+1}=\dots=M^1=M$$
が成り立つ。これより、$M^{e^{-1}\%p^n-p}$が$X$についての方程式$X^e=M$の解の1つになる。
