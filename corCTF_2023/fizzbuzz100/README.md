# fizzbuzz100
category: Crypto  
121 points, 134 solves

## 問題
> lsb oracles are pretty overdone... anyway here's fizzbuzz  
>   
> `nc be.ax 31100`

## 解法
公開鍵と暗号文が渡され、こちらで任意に選んだ暗号文の復号結果がflagでなく $3$ および $5$ の倍数でもなければ復号結果を貰える。平文を $m,$ 公開鍵を $(N,e),$ 暗号文を $c$ とおくと、 $k\cdot m$ を暗号化したものは $k^e\cdot m^e\bmod N=k^ec\bmod N$ である。つまり既知の $e,c$ と任意に選んだ $k$ を用いて計算される $k^ec\bmod N$ の復号結果が分かれば $m$ が求まることになる。 $m,c$ の値に関わらず、 $k$ を $N$ と同程度の桁数で選べば約 $\dfrac8{15}$ の確率で $3$ および $5$ の倍数でなくなる。
