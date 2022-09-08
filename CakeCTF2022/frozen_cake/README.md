# frozen cake
category: Crypto  
88 points, 132 solves

## 問題
> oh your cake is frozen. please warm it up and get the first cake.

## 解法
$n,a=\text{flag}^p\bmod n,b=\text{flag}^q\bmod n,c=\text{flag}^n\bmod n$が与えられている。Eulerの定理より
$$\text{flag}^n\bmod n=\text{flag}^{(p-1)(q-1)}\cdot\text{flag}^{p+q-1}\bmod n=\text{flag}^p\cdot\text{flag}^q\cdot\text{flag}\bmod n$$
であるから、$abc^{-1}=\text{flag}$となる。
