# CoughingFox2
category: Crypto  
58 points, 388 solves

## 問題
> 暗号問題に初めて挑戦する方向けに独自暗号と暗号化した後の出力を配布します。 ご覧の通り、簡易な暗号方式なので解読は簡単です。 解読をお願いします！ 
>  
> The original cipher for beginners and encrypted text are provided. Needless to say, this cipher is too childish, and that easy to decrypt! So, could you please decrypt it?

## 解法
シャッフルされているが、暗号化の第 $i$ ループの出力は(平方数) $+i$ の形になっている。約 $5$ 桁の平方数の間隔は十分に広いので、cipherの各要素から $i$ を引いて平方数かどうか判定すれば第何ループの出力なのか分かる。flagが`ctf4b{`で始まることを使えば復号できる。
