# EZDORSA\_Lv1
category: Crypto  
122 points, 529 solves

## 問題
> はじめまして！RSA暗号の世界へようこそ！
> 
> この世界ではRSA暗号と呼ばれる暗号がいたるところで使われておる！
> 
> それでは手始めに簡単な計算をしてみよう！
> 
> - p = 3
> - q = 5
> - n = p\*q
> - e = 65535
> - c ≡ m^e (mod n) ≡ 10 (mod n)
> 
> 以上を満たす最小のmは何でしょう？
> FLAG{THE\_ANSWER\_IS\_?}の？にmの値を入れてください。

## 解法
「最小の"正整数"$m$」と書くべきなのではと思ったりする。これくらいなら暗算で全探索できそうな気がするが、$e=65537$としないよう注意。