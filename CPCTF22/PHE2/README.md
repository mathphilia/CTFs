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
以下、特に断りがない場合mod n<sup>2</sup>で考える。cを送ったときに何が起こるかを考えよう。まず`onlinepole.vote`がc倍される。もともとの値はいくつであったか見てみると、乱数rを用いてg<sup>100</sup>r<sup>n</sup>と表されることが分かる。その後、`onlinepole.vote`が復号される。具体的には、暗号文vに対して復号結果は  
<div align="center">![数式1](https://github.com/mathphilia/CTFs/blob/main/images/CPCTF22/PHE2_1.png?raw=true)</div>  
である。ここに、λ=lcm(p-1,q-1)であり、μはよく分からない正整数である。よくわからなくても解けるので問題ない。さて、v<sup>λ</sup>%n<sup>2</sup>-1=0になってくれれば復号結果が0になることが分かると思う(もう少し大きくなってもいいかもしれないが)。[Carmichaelの定理](https://ja.wikipedia.org/wiki/フェルマーの小定理#カーマイケルの定理)よりgcd(a,n<sup>2</sup>)=1なるaに対してa^<sup>lcm(p(p-1),q(q-1))</sup>=a<sup>nλ</sup>≡1 (mod n<sup>2</sup>)が成り立つので、vが何らかの数のn乗になってくれればよい。v=cg<sup>100</sup>r<sup>n</sup>であったことを思い出すと、c=g<sup>n-100</sup>とすればよいことが分かる。
