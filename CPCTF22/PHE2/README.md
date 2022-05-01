<script type="text/javascript" async src="https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.7/MathJax.js?config=TeX-MML-AM_CHTML"></script>
<script type="text/x-mathjax-config">
    MathJax.Hub.Config({
        tex2jax: {inlineMath: [['$', '$'], displayMath: [['$$', '$$']]}
    });
</script>

# PHE2
category: Crypto
388.15 points, 8 solves

## 問題
> 新しい電子投票システムを使って、信任投票を行うみたいです。
> この信任投票では、１票でも賛成であれば、承認されます。
> どうやら、この信任投票を阻止すると特別なメッセージを受け取れるらしいです。
> 
> `nc phe2.cpctf.space 30008`

## 解法
以下、特に断りがない場合$\mathrm{mod}\;n^2$で考える。$c$を送ったときに何が起こるかを考えよう。まず`onlinepole.vote`が$c$倍される。もともとの値はいくつであったか見てみると、乱数$r$を用いて$g^{100}r^n$と表されることが分かる。その後、`onlinepole.vote`が復号される。具体的には、暗号文$v$に対して復号結果は
$$\left\lfloor\frac{v^\lambda\%n^2-1}{n\mu}\right\rfloor\%n\quad(\lfloor\cdot\rfloor:\text{floor function})$$
である。ここに、$\lambda=\operatorname{lcm}(p-1,q-1)$であり、$\mu$はよく分からない正整数である。よくわからなくても解けるので問題ない。さて、$v^\lambda\%n^2-1=0$になってくれれば復号結果が0になることが分かると思う(もう少し大きくなってもいいかもしれないが)。[Carmichaelの定理](https://ja.wikipedia.org/wiki/フェルマーの小定理#カーマイケルの定理)より$\gcd(a,n^2)=1$なる$a$に対して$a^{\operatorname{lcm}(p(p-1),q(q-1))}=a^{n\lambda}\equiv1\;(\mathrm{mod}\;n^2)$が成り立つので、$v$が何らかの数の$n$乗になってくれればよい。$v=cg^{100}r^n$であったことを思い出すと、$c=g^{n-100}$とすればよいことが分かる。
