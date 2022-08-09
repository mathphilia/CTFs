# Mino
category: Crypto
169 points, 23 solves

## 問題
> You cannot have a good cryptosystem without mathematics! This task is an easy coding system!  
>   
> `nc 02.cr.yp.toc.tf 13771`

## 解法
**この解法の正当性に関する証明は一切していません。なんとなくで解いた結果ですのであしからず。**
とりあえず接続してみると
> Hi crypto programmers! I'm looking for some very special permutation p name MINO such that sum(p(i) \* (-2)^i) = 0 from 0 to n - 1, for example for n = 6, the permutation p = (4, 2, 6, 5, 3, 1) is MINO: 4\*(-2)^0 + 2\*(-2)^1 + 6\*(-2)^2 + 5\*(-2)^3 + 3\*(-2)^4 + 1\*(-2)^5 = 0 In each step find such permutation and send to server, if there is NOT such permutation for given n, just send \`TINP', good luck :)

と言われる。つまり、$n$項数列$p_0,p_1,p_2,\dots,p_{n-1}$であって
$$\{p_0,p_1,p_2,\dots,p_{n-1}\}=\{1,2,3,\dots,n\}$$
$$\sum_{i=0}^{n-1}p_i\cdot(-2)^i=p_0-2p_1+4p_2-\dots+(-2)^{n-1}p_{n-1}=0$$
を満たすものを見つければよい。なお、一般には条件を満たす数列$p$は$1$通りでなく(例えば$n=9$の解は$379$通り)、$n\equiv1\pmod3$の場合は解が存在しない($\bmod3$で考えれば容易に示せる)。$n=9$くらいなら全探索できるが、最終的には$n=40$の場合を解くことが必要になる。$n=9$まで計算してみると、例えば$n=5$の解と$n=6$の解の冒頭部分が一致している、といったことが起こっている。よって、$1$つ前の$n$における解の後半部分のみ変えればよさそうである。[solver.py](CryptoCTF2022/Mino/solver.py)では末尾4項以外を固定した。
