# switchable\_cat
category: Crypto  
179 points, 27 solves

## 問題
> 暗号化アルゴリズムをつくったよ 
> あ！さっそくねこちゃんが平文を暗号化しにきたよ！ 
> かわいいね！！！！

## 解法
LFSRもどきの問題。`LFSR`オブジェクトが`ord("🐈")*ord("🐈")*ord("🐈")*8` bitの疑似乱数を出力した後の内部状態を計算する。疑似乱数には詳しくないのでいろいろ検索した結果、LFSRの内部状態の変化は線型写像で書けることが分かった(原始多項式云々に気をとられて失念していたが、名前からして当たり前)。今回の疑似乱数生成器には`switch`がくっついているが、やっていることはほぼLFSRと同じ。$k$ bit出力した直後の`self.rr`の値を、最上位ビットの値が第 $0$ 成分, 最下位成分の値が第 $127$ 成分となるような列ヴェクトルで表現し、変数 $r_k$ で表す。このとき次の式が成り立つ。

$$r_1=Ar_0,\;r_2=Br_1=BAr_0,\;r_3=ABAr_0,\;r_4=BABAr_0,\;\dots$$
$$r_k=\begin{cases}(BA)^{k/\!/2}&(k:\text{even})\\A(BA)^{k/\!/2}&(k:\text{odd})\end{cases}$$

ただし計算はすべて$\bmod2$の下で行われるものとし、

$$A=\begin{pmatrix}0&0&0&\cdots&1&0&0&1&0&1&0&1&0&1\\1&0&0&\cdots&0&0&0&0&0&0&0&0&0&0\\0&1&0&\cdots&0&0&0&0&0&0&0&0&0&0\\0&0&1&\cdots&0&0&0&0&0&0&0&0&0&0\\\vdots&\vdots&\vdots&\ddots&\vdots&\vdots&\vdots&\vdots&\vdots&\vdots&\vdots&\vdots&\vdots&\vdots\\0&0&0&\cdots&0&0&0&0&0&0&0&1&0&0\\0&0&0&\cdots&0&0&0&0&0&0&0&0&1&0\\0&0&0&\cdots&0&0&0&0&0&0&0&0&0&1\end{pmatrix}$$
$$B=\begin{pmatrix}0&0&0&\cdots&0&1&1&0&1&0&0&0&1&0\\1&0&0&\cdots&0&0&0&0&0&0&0&0&0&0\\0&1&0&\cdots&0&0&0&0&0&0&0&0&0&0\\0&0&1&\cdots&0&0&0&0&0&0&0&0&0&0\\\vdots&\vdots&\vdots&\ddots&\vdots&\vdots&\vdots&\vdots&\vdots&\vdots&\vdots&\vdots&\vdots&\vdots\\0&0&0&\cdots&0&0&0&0&0&0&0&1&0&0\\0&0&0&\cdots&0&0&0&0&0&0&0&0&1&0\\0&0&0&\cdots&0&0&0&0&0&0&0&0&0&1\end{pmatrix}$$

とおく。 $N$ 乗の計算は $O(\log N)$ で行えるので、`ord("🐈")*ord("🐈")*ord("🐈")*8` bitの疑似乱数を出力した後の内部状態を短時間で算出できる。