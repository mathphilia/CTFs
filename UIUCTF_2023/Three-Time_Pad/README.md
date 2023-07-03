# Three-Time Pad
category: Crypto  
50 points, 309 solves

## 問題
> "We've been monitoring our adversaries' communication channels, but they encrypt their data with XOR one-time pads! However, we hear rumors that they're reusing the pads...  
>   
> Enclosed are three encrypted messages. Our mole overheard the plaintext of message 2. Given this information, can you break the enemy's encryption and get the plaintext of the other messages?"

## 解法
`c2`と`p2`のXORをとったものが`c2`の暗号化鍵であり、`c1`,`c3`の暗号化鍵もこれと同一であると問題文に書かれている。したがって`c2 xor p2`を鍵として`c1`,`c3`を復号すればよい。
