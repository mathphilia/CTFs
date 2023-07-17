# easy factoring
category: Crypto  
102 points, 95 solves

## 問題
> The word "decomposition" has multiple meanings.  
> Can you decompose?  
> `nc crypto.2023.zer0pts.com 10333`

## 解法
整数 $N$ が与えられて $N=p^2+q^2$ なる素数 $p,q$ を求める問題。与えられた正整数を $2$ つの平方数の和で表す方法は[tsujimotterさんの記事](https://tsujimotter.hatenablog.com/entry/fermat-descent)を参考に実装する。ここで注意すべきは、何も考えずに実装すると $N=p^2+q^2$ を満たす**整数**の組 $(p,q)$ が**一組**得られるだけだ、ということ。[今回のsolver](https://github.com/mathphilia/CTFs/blob/main/zer0pts_CTF_2023/easy_factoring/solver.py)では $N$ の各素因数を平方数に分解する方法を一組見つけた後、符号を変えながら $N$ の分解を色々見つけている。これで所望する $p,q$ が必ず見つかることの証明はしていないが、何度か試した中では毎回求まったので多分大丈夫だと思っている。なお、 $N$ は256bitあるので必ずしも素因数分解できるとは言えないが、それほど低くない確率で完全な素因数分解が求まる。
