# PrimeParty
category: Crypto  
127 points, 58 solves

## 問題
> Primeパーティへようこそ！！！  
> `nc primeparty.quals.beginners.seccon.jp 1336`

## 解法
サーバ側で生成される素数$p_1,p_2,p_3,p_4$とこちらが提示する素数$p_5,p_6,p_7$に対し、$N=p_1p_2p_3p_4p_5p_6p_7,e=65537$でflagを暗号化したものを教えてもらえる。暗号文を$c$とすると、$c$は$\texttt{flag}^e$を$N$で割った余りなので、整数$k$を用いて$c=\texttt{flag}^e-kN$と書ける。$N$が$p_5$の倍数であることに注意すると$c\%p_5=(\texttt{flag}^e-kN)\%p_5=\texttt{flag}^e\%p_5$なので、$c\%p_5$は$p_5$をmodulus, $e$をpublic exponentとしてflagを暗号化したものである。つまり、$p_1,p_2,p_3,p_4$に関係なく$c,e,p_5$の情報のみで$\texttt{flag}\%p_5$を復元できる。flagが455bitsなので、$p_5$を456bits以上となるようにとればflagを復元できる。solverでは事前に$2^{512}$の次の素数を生成しておいた。
