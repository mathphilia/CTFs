# Welcome
category: Frosty
228 points, 39 solves

## 問題
> I just found this great new multisignature scheme, we can collaborate to sign messages together!
> ```
> nc frosty.nc.jctf.pro 4444
> ```
> - PS: The connections are dropped automatically after 4 minutes.
> - https://s3.cdn.justctf.team/95aa7604-1b77-4a71-8528-a7f854b57d8a/frosty.py

## 解法
`genkey`で鍵を生成して`sign`で署名し、`verify`に投げればよいように見えるが、`genkey`函数の
```py
registered_keys[public_key] = sk
```
の部分において、`public_key`がunhashableなPoint型なのでTypeErrorが生じる。従って署名は手元で生成しなければならない。`genkey`函数と`sign函数を書き換えて使ってもよいが、仕組みを理解するためにあえてこれらは使わずに解く。`sign`函数を見ると、pubkeyとmを受け取り$R$を生成→$c$を生成→$z$を生成 という手順を踏んで、最終的に$R=zG-cP$ ($G$: Curve.G, $P$: pubkey)と$c=\operatorname{mod\_hash}(m,R)$が満たされるようにしている(正確には`sign`函数の出力にクライアント側のsecret nonceを足したものが条件を満たす$z$になる)。手元で署名を生成する際もこの手順に則って考えてみる。まず$m$は`b'Gimme!'`であり、$P$と$R$は適当に決める。ただし、それぞれが$G$の何倍であるかは把握しておく。[solver.py](Frosty/solver.py)では$P=R=G$とした。$m,R$が定まれば$c=\operatorname{mod\_hash}(m,R)$により$c$が定まる。最後に$R=zG-cP\Leftrightarrow zG=cP+R$から$z$が求まる。$P=R=G$なら$zG=cG+G=(c+1)G$なので$z=c+1$とすれば`verify`を通る。
