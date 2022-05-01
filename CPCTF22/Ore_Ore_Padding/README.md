# Ore Ore Padding
category: Crypto  
444.39 points, 4 solves

## 問題
> オレのパディングを使えばセキュアに通信できるぞ！  
> `nc ore-ore-padding.cpctf.space 30003`

## 解法
送信した暗号文を復号したときの値が$n/2$未満であるか否かを教えてくれる。k<sup>e</sup>cを復号するとkm%nになるため、mの定数倍をnで割った余りがn/2未満であるか否かは分かることになる。1回のやり取りで得られる情報は`ok`が来るか`padding error`が来るかなので2通り。つまり2分探索のようなものができるのではないかと推測できる。2<sup>r</sup>m%nとn/2の大小を調べると
```
n = 55, m = 36
r            0  1  2  3  4  5
2ʳ*m % n    36 17 34 13 26 52
n/2 < 2ʳ*m   o  x  o  x  x  o
```
となる。中段の2<sup>r</sup>m%nを割り算を使わない形で表してみよう。36はm。17は2mをnで割った余りだが、n以下の未満の正整数を2倍して2n以上になることはないので2m-nになる。34はその2倍なので4m-2n。13は17のときと同様に考えて2(4m-2n)-n=8m-5n。以下同様にして、26=2(8m-5n)=16-10n, 52=2(16m-10n)=32m-20nとなる。ここで、n/2 < 52 < nであるので  
<div align="center"><img src="https://github.com/mathphilia/CTFs/blob/main/images/CPCTF22/Ore_Ore_Padding_1.png?raw=true"></div>  
が分かる。これにn=55を代入すると35.23… < m < 26.09…が分かり、m=36を得る。同様にしてm=47の場合もやってみよう。
```
n = 55, m = 47
r            0  1  2  3  4  5
2ʳ*m % n    47 39 23 46 37 19
n/2 < 2ʳ*m   o  o  x  o  o  x
```
となるので、47=m, 39=2m-n, 23=4m-3n, 46=8m-6n, 37=16m-13n, 19=32m-27nで  
<div align="center"><img src="https://github.com/mathphilia/CTFs/blob/main/images/CPCTF22/Ore_Ore_Padding_2.png?raw=true"></div>  
即ちm=47を得る。  
2つの計算の下から2行目(∴のところ)において、左辺の分子に乗っている数に注目しよう。これは計算の過程から「表の下段の`o`を1に、`x`を0に置き換え、2進数として解釈したもの」に等しい。例えばm=36の方では101001<sub>(2)</sub>=41、m=47の方では110110<sub>(2)</sub>=54である。以上の方法を使うことによりmを求めることができる。なお、問題プログラムの
```py
while m < n // 2:
    plaintext = get_random_bytes(remain - 1) + b'\x00' + plaintext
    m = bytes_to_long(plaintext)
```
の部分でn < mとなってしまうせいだと思うが、1/2の確率でflagを得ることに失敗する。
