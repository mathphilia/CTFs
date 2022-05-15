# MOO
category: Crypto
58 points, 64 solves

## 問題
> One of the cows in our farm started to say weird numbers instead of MOOing, can you guess what it's saying?  
>   
> `nc challs.m0lecon.it 1753`

## 解法
Nの倍数でないような任意の入力gに対し、`f2(g, (p, q), (pfs, qfs))`を教えてもらえる。`f2`が何をしているか見てみると、`f1(g, p, pfs)`と`f1(g, q, qfs)`のLCMをとっている。`f1`が何をしているか見てみると、g<sup>k<sub>p</sub></sup>%p=1となるようなkを探している。`f2(g, (p, q), (pfs, qfs))`=lcm(k<sub>p</sub>, k<sub>q</sub>)は`f1(g, p, pfs)`=k<sub>p</sub>の倍数であるから、g<sup>lcm(k<sub>p</sub>, k<sub>q</sub>)<sub>をpで割った余りは1になる。同様にしてqで割った余りも1になるので、g<sup>lcm(k<sub>p</sub>, k<sub>q</sub>)<sub>をNで割った余りは1になる。これはRSA暗号の復号過程におけるφ(N)と同等の働きをしてくれることが期待される。しかし、**Z**/N**Z**上のgの位数がcの位数より小さいときは上手くいかないので数回のチャレンジが用意されている。
