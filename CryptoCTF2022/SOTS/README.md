# SOTS
category: Crypto
49 points, 113 solves

## 問題
> He who abides far away from his home, is ever longing for the day he shall return.  
>   
> `nc 05.cr.yp.toc.tf 37331`

## 解法
$4n+1$型素数を2つの平方数の和で表すプログラムは[tsujimotterさんの解説](https://tsujimotter.hatenablog.com/entry/fermat-descent)を参考にして実装すればよい。合成数の場合、その数が平方因子を含まない奇数であれば以下のようにして2平方和に分解できる(この条件を満たす合成数が2平方和で表せるための必要十分条件は素因数がすべて$4n+1$型であることに注意)。  
$N=p_1p_2p_3\dots p_n$を2平方和に分解するとしよう。上述の通り$p_1,p_2,p_3,\dots,p_n$は2平方和に分解できる。この分解を$p_i=a_i^2+b_i^2$と書く。さて、$p_1p_2=(a_1^2+b_1^2)(a_2^2+b_2^2)$と書けるわけだが、tsujimotterさんの解説でも紹介されていたBrahmaguptaの恒等式を使うとこれは$p_1p_2=(a_1a_2+b_1b_2)^2+(a_1b_2-a_2b_1)^2$と変形できる。つまり$p_1p_2$を2平方和で表すことができた。同様にして$p_1p_2p_3$を2平方和で表し、$p_1p_2p_3p_4$を2平方和で表し、…とすることにより最終的に$N$を2平方和に分解できる。  
なお、この方法では$N$を素因数分解する操作が必須だが、この問題における$N$は80bit程度の素数3つの積で表されているため、Msieveを使うなどしないと素因数分解は困難であろう。
