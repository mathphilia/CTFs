<script type="text/javascript" async src="https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.7/MathJax.js?config=TeX-MML-AM_CHTML"></script>
<script type="text/x-mathjax-config">
    MathJax.Hub.Config({
        tex2jax: {inlineMath: [['$', '$'], displayMath: [['$$', '$$']]}
    });
</script>

# Ore Ore Padding
category: Crypto
444.39 points, 4 solves

## 問題
> オレのパディングを使えばセキュアに通信できるぞ！
> `nc ore-ore-padding.cpctf.space 30003`

## 解法
送信した暗号文を復号したときの値が$\dfrac n2$未満であるか否かを教えてくれる。$k^ec$を復号すると$km\%n$になるため、$m$の定数倍を$n$で割った余りが$\dfrac n2$未満であるか否かは分かることになる。1回のやり取りで得られる情報は`ok`が来るか`padding error`が来るかなので2通り。つまり2分探索のようなものができるのではないかと推測できる。$2^rm%n$と$\dfrac n2$の大小を調べると
```
n = 55, m = 36
r           0  1  2  3  4  5
2^r*m % n  36 17 34 13 26 52
n/2<2^r*m   o  x  o  x  x  o
```
となる。中段の$2^rm\%n$を割り算を使わない形で表してみよう。$36$は$m$。$17$は$2m$を$n$で割った余りだが、$n$以下の未満の正整数を2倍して$2n$以上になることはないので$2m-n$になる。$34$はその2倍なので$4m-2n$。$13$は$17$のときと同様に考えて$2(4m-2n)-n=8m-5n$。以下同様にして、$26=2(8m-5n)=16-10n,52=2(16m-10n)=32m-20n$となる。ここで、$\dfrac n2<52<n$であるので
$$\frac n2<32m-20n<n$$
$$\therefore\frac{41}{64}n<m<\frac{42}{64}n$$
が分かる。これに$n=55$を代入すると$35.23\ldots<m<26.09\ldots$が分かり、$m=36$を得る。同様にして$m=47$の場合もやってみよう。
```
n = 55, m = 47
r           0  1  2  3  4  5
2^r*m % n  47 39 23 46 37 19
n/2<2^r*m   o  o  x  o  o  x
```
となるので、$47=m,39=2m-n,23=4m-3n,46=8m-6n,37=16m-13n,19=32m-27n$で
$$0<32m-27n<\frac n2$$
$$\therefore\frac{54}{64}n<m<\frac{55}{64}n$$
即ち$m=47$を得る。
2つの計算の下から2行目($\therefore$のところ)において、左辺の分子に乗っている数に注目しよう。これは計算の過程から「表の下段の`o`を1に、`x`を0に置き換え、2進数として解釈したもの」に等しい。例えば$m=36$の方では$101001_{(2)}=41$、$m=47$の方では$110110_{(2)}=54$である。以上の方法を使うことにより$m$を求めることができる。なお、問題プログラムの
```py
while m < n // 2:
    plaintext = get_random_bytes(remain - 1) + b'\x00' + plaintext
    m = bytes_to_long(plaintext)
```
の部分で$n<m$となってしまうせいだと思うが、$\dfrac12$の確率でflagを得ることに失敗する。
