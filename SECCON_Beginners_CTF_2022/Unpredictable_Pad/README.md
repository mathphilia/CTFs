# Unpredictable Pad
category: Crypto  
159 points, 35 solves

## 問題
> CSPRNGじゃなければ予想できるって聞きました。  
> `nc unpredictable-pad.quals.beginners.seccon.jp 9777`

## 解法
$2^{64}$以下のinputに対し、getrandbits(input.bit\_length()) xor inputを教えてもらえるということが3回行われる。getrandbits(32)を624回分見ると[predict.py](predict.py)の方法によってそれ以降の疑似乱数を予測できる(参考: [Mersenne Twisterの出力を推測してみる - ももいろテクノロジー](https://inaz2.hatenablog.com/entry/2016/03/07/194147))。また、
$$\operatorname{getrandbits}(32n)=\sum_{k=0}^{n-1}\operatorname{getrandbits}(32)\cdot(2^32)^k$$
なのでgetrandbits(32×624)の値が分かればそれ以降の疑似乱数を予測できる。一見したところ、input.bit\_length()が64以下であるのでgetrandbitsの中身は64以下となり、3回教えてもらっても192bits、つまりgetrandbits(32)を6回教えてもらった場合と同じ情報量にしかならない。しかし、inputを負にしてみるとどうだろうか。例えば(-13).bit\_length()は4というように、n.bit\_length()と(-n).bit\_length()は等しくなる。つまり、絶対値が非常に小さい負の数のbit lengthは非常に大きくなるので、inputを$-(2^{32\times624}-1)$とすればgetrandbits(32×624)を教えてもらえることになる。
