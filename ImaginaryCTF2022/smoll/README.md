# smoll
category: Crypto
100 points, 226 solves

## 問題
> Just a regular, run-of-the-mill RSA challenge, right? Right?

## 解法
$p-1$と$q-1$の素因数が高々$20$bitであるから$p-1$法が使えそうである。しかし、boundをどのように設定してもうまくいかない。$p-1$の最大素因数と$q-1$の最大素因数が一致しているようである。さてどうしたものだろうか…と思っていたら、点数が最低点である100点になっていたのでもしやと思って[factordb.com](http://factordb.com/index.php?id=1100000003760454151)に突っ込んでみると素因数分解できてしまった。明らかに想定解でないので、出題側のミスなのか参加者がやらかしたのか分からないが、なんとも興ざめである(いまだに正攻法を思いついていないので点数的にはオトクだったが)。
