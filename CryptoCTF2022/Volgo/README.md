# Volgo
category: Crypto
65 points, 77 solves

## 問題
> There is no land behind the Volga!! The Soviets surround us,and we have only a single key table to communicate to the outside!! Hopefully, the Soviets wouldn't be able read our messages.  
>   
> `http://03.cr.yp.toc.tf:11117/`

## 解法
M-209という暗号システムによる暗号化をしてくれるサイトが渡される。M-209に関する情報を探しても見つからないので実際にいろいろな入力を試してみる。すると以下のことが分かる。  
- 暗号文の先頭5文字及び末尾5文字は平文によらず一定である。
- 暗号文の正味の(先頭及び末尾5文字を除いた)部分の文字数は5の倍数である。
- そのうち平文の文字数より多い部分は`X`でパディングされる(例: `ABC`→`PQR`と暗号化されたら暗号文の正味の部分は`ABCXX`となる)。

恐らく多表換字式暗号であり$n$文字目の暗号文は平文の$n$文字目までのみによって($n+1$文字目以降には依らず)決定するであろうと予測して、1文字目から順に全探索する。得られた平文は英文の' 'を'Z'に置き換えたものになっている。
