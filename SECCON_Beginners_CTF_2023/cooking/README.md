# cooking
category: Crypto  
221 points, 17 solves

## 問題
> Let's Cooking! 
>  
> `nc cooking.beginners.seccon.games 1337`

## 解法
作問ミスがあったようで、超簡単な非想定解で解けてしまった。想定解法は[こちら](https://qiita.com/Anko_9801/items/3136c49de4c013cde9a5)。23行目の 

```
print("This is meat:", pow(meat, pepper, p))
```

の出力がただのRSA( $N$ が素数だけど)なので、簡単に`meat` $\bmod p$ が求まってしまう。`pepper`が $3$ なので $p-1$ が $3$ の倍数でないような $p$ を選ぶとよい。また、`meat` $\bmod p$ がほぼ確実に`meat`に一致するようにするため、 $p$ は $2^{2048}$ に近い方がよい。以上の条件を満たす素数 $p$ をMiller-Rabin法などを使って探し、`meat`を求める。 $p$ と`meat`以外は適当な値を送っておけばよい。
