# PHE1
category: Crypto
184.28 points, 43 solves

## 問題
> 秘密鍵を持ってることを秘密鍵なしで証明するハッピーな方法を考えたッピ！
> 
> `nc phe1.cpctf.space 30007`

## 解法
$a,b$をそれぞれ暗号化したもの与えるので$ab$を暗号化したものを求めよ、という問題。暗号化の手順を考えると
$$\operatorname{encrypt}(ab)\equiv(ab)^e=a^eb^e\equiv\operatorname{encrypt}(a)\operatorname{encrypt}(b)\;(\mathrm{mod}\;N)$$
となるので暗号文の積が答えとなる。
