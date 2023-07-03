# Morphing Time
category: Crypto  
50 points, 140 solves

## 問題
> The all revealing Oracle may be revealing a little too much...  
>   
> `nc morphing.chal.uiuc.tf 1337`

## 解法
平文を $m$ とすると、暗号文は秘密鍵 $a$ と乱数 $k$ を用いて $(c_1,c_2)=(g^k,g^{ak}m)$ となっている( $\bmod p$ で)。復号は $c_1^ac_2^{-1}$ を計算する。問題名がMorphing Timeなのでhomomorphicな感じなのかなと思いつつ平文 $m=1$ および乱数 $k=1$ に対応する暗号文 $(g,g^a)$ を送信するとどうなるか考えると、flagがそのまま返ってくると分かる。したがって $g,A$ を送信するのが正解。
