# Klamkin
category: Crypto
61 points, 83 solves

## 問題
> We need to have a correct solution!  
>   
> `nc 04.cr.yp.toc.tf 13777`

## 解法
自然数$q,r,s$が与えられた上で、「$(ar+bs)\bmod q=0$を満たす任意の(整数)$a,b$に対し、常に$(ax+by)\bmod q=0$となる」ような整数$x,y$を答えるよう求められる。ただし、「$x$は$12$bit」のような制約が課される。以下では$r,s$が$q$と互いに素な場合を考える(実際、$q$が素数であるものしか出題されていない)。$(ar+bs)\bmod q=0\Leftrightarrow b=-rs^{-1}a\pmod q$であるから、$(ax+by)\bmod q=a(x-rs^{-1}y)=0$である。$a$は任意であったから、$x-rs^{-1}y=0$でなければならない。逆に、この等式が満たされていれば$x,y$は問題の条件を満たす。
