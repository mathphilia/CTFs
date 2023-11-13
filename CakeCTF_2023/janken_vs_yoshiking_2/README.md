# janken vs yoshiking 2
category: Crypto  
144 points, 43 solves

## 問題
> the newest version of janken-vs series is coming! `nc crypto.2023.cakectf.com 10555`

## 解法
100回連続でじゃんけんに勝利するとflagを貰える。じゃんけんの手を事前に決めていることを示すために署名的なことをしている。まず大きな素数 $p$ および $\mathbb F_p$ 上の $5$次正方行列を提示する。3種類の手に整数 $1,2,3$ を対応させ、出す予定の手に対応する数を $m$ として $m\equiv r+1\pmod3$ を満たす乱数 $r$ ( $2\leqq r\leqq2^{256}$ )を試合毎に生成し、 $C=M^r$ を見せる。自分が勝ったら $r$ を公開することでインチキがないことを証明する。 $C^r$ から $r\bmod3$ を求めればよいので、 $M\in\operatorname{GL}_5(\mathbb F_p)$ の位数を $n$ として $M^{0n/3},M^{n/3},M^{2n/3}$ が異なることを使うことが考えられる(もっと言えば $n$ は位数×( $3$ の倍数でない数)であればよい)。 $\operatorname{GL}_5(\mathbb F_p)$ の位数は $\displaystyle\prod_{k=0}^4(p^5-p^k)$ である(証明略)ので $M$ の位数はこれの約数である。SageMathの実行環境をローカルに持っていないのでNumpyを使って $\mathbb F_p$ の行列累乗を実装した。  
ところで今回の $p$ は $379$ 以下の素数の積に $1$ を加えた値であり安全素数とは程遠い状態になっている。これを使うと $M$ の位数がより小さくなると考えられる。そんなことを考えなくても解けるのでそんなことは考えずに解いたが。