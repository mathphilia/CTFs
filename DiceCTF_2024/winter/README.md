# winter
category: Crypto  
116 points, 169 solves

## 問題
> A simple implementation of the Winternitz signature scheme.  
> `nc mc.ax 31001`

## 解法
署名の問題。32bytesの乱数32個を秘密鍵として、以下の手順で署名および検証を行う。  

- 署名
    1. メッセージ $m$ をSHA256でハッシュ化し、出力の32bytesを上位の桁から順に $a_0,a_1,\dots,a_{31}$ とおく。  
    2. $i=0,1,\dots,31$ に対し、秘密鍵の $i$ 番目をSHA256で $(256-i)$ 重にハッシュ化したものを $b_0,b_1,\dots,b_{31}$ とする。  
    3. $(b_0,b_1,\dots,b_{31})$ を署名とする。  
- 検証
    1. メッセージ $m$ をSHA256でハッシュ化し、出力の32bytesを上位の桁から順に $a_0,a_1,\dots,a_{31}$ とおく。  
    2. $i=0,1,\dots,31$ に対し、署名の $i$ 番目をSHA256で $i$ 重にハッシュ化したものを $b_0,b_1,\dots,b_{31}$ とする。  
    3. 秘密鍵の各項をSHA256で $256$ 重にハッシュ化したものが $(b_0,b_1,\dots,b_{31})$ と一致した場合署名を正当なものと判定する。  

この問題では、こちらが与えたメッセージに対して署名が返され、別のメッセージおよびそのに適合する署名を答えられればflagを貰える。秘密鍵を $(s_0,s_1,\dots,s_{31})$ とし、 $s_i$ を $k$ 重にハッシュ化したものを $s_i^{(k)}$ とする。最初に投げるメッセージのハッシュを $(h_0,h_1,\dots,h_{31})$ 、次に投げるメッセージのハッシュを $(h_0',h_1',\dots,h_{31}')$ としたら、第一メッセージで生成された署名を第二メッセージで検証したら $(s_0^{(256-h_0+h_0')},s_1^{(256-h_1+h_1')},\dots,s_{31}^{(256-h_{31}+h_{31}')})$ と $(s_0^{(256)},s_1^{(256)},\dots,s_{31}^{(256)})$ が比較されることになる。したがって $h_i=h_i'$ であればよいが、これはハッシュ衝突を意味することになり発見は難しい。しかし $h_i'<h_i$ を仮定すると、 $s_i^{(256-h_i)}$ を更に $(h_i-h_i')$ 重にハッシュ化したものを $s_i'$ とすることで $(s_0',s_1',\dots,s_{31}')$ を 第二メッセージの署名とできることが分かる。  
以上より、全ての $i$ について $h_i'<h_i$ となるようなメッセージの組を見つけることになる。2つのメッセージをランダムに選んだ時、全ての $i$ について $h_i'<h_i$ となる確率は $2^{-32}$ である。よって愚直に考えると単純計算で $2^{32}$ 回のハッシュ比較をすることになり、時間がかかりすぎる。そこで、 $h_i$ の値が全体的に小さいメッセージと全体的に大きいメッセージ(と中庸なメッセージ)に分類し、小さいグループと大きいグループだけで比較することにより計算回数を節約することができる。具体的に、今回の[solver](https://github.com/mathphilia/CTFs/blob/main/DiceCTF_2024/winter/solver.py)では「全ての $i$ について $64<h_i$ 」「全ての $i$ について $h_i<192$ 」(とその他)に分類した。 $N$ 個のメッセージの場合各グループの要素数は約 $\left(\dfrac34\right)^{32}N\fallingdotseq\dfrac N{10000}$ となる。また、「全ての $i$ について $64<h_i'$ 」を満たすメッセージと「全ての $i$ について $h_i<192$ 」を満たすメッセージの比較において全ての $i$ について $h_i'<h_i$ となる確率は約 $\left(\dfrac79\right)^{32}\fallingdotseq\dfrac1{3000}$ である。よって、概ね  
$$3000<\left(\dfrac N{10000}\right)^2\text{ i.e. }550000<N$$  
を満たす程度の個数のメッセージを使えば条件を満たすメッセージが見つかり、分類・比較を含め現実的な時間で処理が終わることになる(実際は余裕をもって $2^{20}$ 個のメッセージを使用した)。