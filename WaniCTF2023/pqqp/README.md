# pqqp
category: Crypto  
165 points, 156 solves

## 問題
> ✨

## 解法
$n,e,c$の他に、$s=(p^q+q^p)\bmod n$が渡される。$n$は$p$の倍数なので$s\bmod p=(p^q+q^p)\bmod p=q^p\bmod p=q$ ($\because$Fermatの小定理)同様に、$s\bmod q=p$である。$p$で割って$q$余り$q$で割って$p$余る数の$1$つに$p+q$がある。中国剰余定理よりこの条件を満たす整数は$\bmod pq$の範囲で一意なので、$s=p+q$である。したがって$p+q$と$pq$が求まったので$p,q$が分かる。
