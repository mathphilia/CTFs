# Group Project
category: Crypto  
50 points, 232 solves

## 問題
> In any good project, you split the work into smaller tasks...  
>   
> `nc group.chal.uiuc.tf 1337`

## 解法
Diffie-Hellman鍵共有のようなことをしている。 $S=g^{abk}\bmod p$ だが、 $b$ も $g^b$ も未知なので確定できない。 $k$ として $\dfrac{p-1}2$ が拒否されている理由を考えると、 $g^{(p-1)/2}\bmod p=1$ になりやすいためであると考えられる。ここで $k$ を $p-1$の正の約数であって $1,p-1,\dfrac{p-1}2$ でないものにしてみる。 $d=\dfrac{p-1}k$ とおくと $(g^{k})^d\bmod p=1$ であり、したがって $S=g^{ki}\bmod p$ を満たす整数 $i$ が $0\leqq i<d$ の範囲に存在する。 $d$ の値は十分小さいことが期待されるので全探索可能である。なお、この方法は[Group Projection](https://github.com/mathphilia/CTFs/tree/main/UIUCTF_2023/Group_Projection)を解くのにも使えるので恐らく想定解ではない。 $k=0$ とすれば $S=1$ になるのでおそらくこれが想定。
