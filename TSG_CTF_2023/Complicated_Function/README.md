# Complicated Function
category: Crypto  
117 points, 70 solves

## 問題
> みんな `q = p + 8` みたいに簡単な式で `q` を決めるからハックされちゃうんだよ。こんなふうに複雑な関数で `p` から `q` を計算してやれば…  
> 初心者向けのヒント:  
> - `challenge.py` の実行結果が `output.txt` に保存されています。  
> - `challenge.py` を読んでみると、 `secrets.py` から `flag` という値を読み込み、暗号化して出力していることがわかります。`secret.py` は配布ファイルに含まれていないので、 `challenge.py` とその出力から、 `flag` の中身を突き止めてやりましょう！
> - `flag` は文字列（正確にはバイト列）ですが、暗号化するために `m = int.from_bytes(flag, 'big')` というコードで対応する整数に変換しています。この `m` を求めることができれば、 `m.to_bytes((m.bit_length()-1)//8 + 1, 'big')` というコードでもとの `flag` を得ることができます。

## 解法
複雑な函数とやらを見てみると、  

$$q=\left\lfloor\sqrt{p^2+(2^{512}-6)+\big\lceil\lfloor\sqrt p\rfloor\sin p\rceil}\right\rfloor+2^{1023}$$  

により $q$ を定めている(概算する上では $\lfloor\phantom m\rfloor$ や $\lceil\phantom m\rceil$ は無視してよい)。 $p$ は1024bitなので $\sqrt p\sin p<(2^{511}-3)^2$ が分かり、したがって $q$ は $p+(2^{511}-3)+2^{1023}$ より少し小さい。誤差は全探索可能な範囲に収まっているので、2次方程式 $p^2+(q-p)p-N=0$ を解けば $p$ が求まり素因数分解に成功する。
