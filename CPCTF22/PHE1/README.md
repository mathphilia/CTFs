# PHE1
category: Crypto  
184.28 points, 43 solves

## 問題
> 秘密鍵を持ってることを秘密鍵なしで証明するハッピーな方法を考えたッピ！
> 
> `nc phe1.cpctf.space 30007`

## 解法
a, bをそれぞれ暗号化したもの与えるのでabを暗号化したものを求めよ、という問題。暗号化の手順を考えると  
encrypt(ab)≡(ab)<sup>e</sup>=a<sup>e</sup>b<sup>e</sup>≡encrypt(a)encrypt(b) (mod N)  
となるので暗号文の積が答えとなる。
