# Roulette
category: Crypto
150 points, 7 solves

## 問題
> ルーレットで一攫千金だ！おいおい、そんなにルーレットを見つめられても困るぜ？なんたってこれはランダムに作ってるんだからな！  
> `nc chall.live.ctf.tsg.ne.jp 61234`

## 解法
<span style="color: red;">注意: この解法は多くの回数netcatする必要があるため、正規の方法でない恐れがあります。</span>  
まずは何回まで失敗できるかを考える。36<sup>4</sup>=1,679,616であるので、3回は失敗できる。線型合同法による疑似乱数の出力を予測する際、modが分かっていれば3個の出力で以降の出力を予測できるが、分かっていない場合は6個の出力を要する(と思う)。`rng.r`が37の倍数であるとき、`rng.next`の出力はmod 37の線型合同法に従う`rng.r`が37の倍数になることを願って何度もnetcatを繰り返す。  
`rng.r`が37の倍数である場合について考えよう。p=`rng.p`,q=`rng.q`とし、n回目の出力をx<sub>n</sub>とする。このときx<sub>n+1</sub>=px<sub>n</sub>+q (mod 37)であるから、以下のようにしてp,qが求まる。
<div align="center"><img src="https://github.com/mathphilia/CTFs/blob/main/images/TSGLIVE8CTF/Roulette_1.png?raw=true"></div>
pとqさえ求まれば{x<sub>n</sub>}は簡単に求まる。
