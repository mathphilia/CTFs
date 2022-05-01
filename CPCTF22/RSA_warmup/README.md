# RSA warmup
category: Crypto  
10.00 points, 72 solves

## 問題
> 多くの秘密を守る為、現代ではRSA暗号がよく使われています。そこでRSA暗号の仕組みについて問う問題です。  
RSA暗号とは剰余上の累乗を使った暗号です。具体的には暗号化は次のようにして計算します。  
> 1. 素数p, qを生成してN=pqを計算  
> 1. 平文mに対して暗号文cはc≡m<sup>e</sup> (mod N)  
> 例えば  
> <div align="center"><img src="https://github.com/mathphilia/CTFs/blob/main/images/CPCTF22/RSA_warmup_1.png?raw=true"></div>  
> とすると暗号文cはc=7<sup>3</sup>=11 (mod 38)となります。  
> 
> それでは逆に復号化はどうやってやるのでしょうか？暗号文とe, Nを与えるので平文をフラグの中に書いて提出してください。例えば平文が1であれば`CPCTF{1}`と書きます。  
> <div align="center"><img src="https://github.com/mathphilia/CTFs/blob/main/images/CPCTF22/RSA_warmup_2.png?raw=true"></div>  

## 解法
どうやってやるのでしょうか？知らない方は[Wikipedia](https://ja.wikipedia.org/wiki/RSA暗号#暗号方式)を見よう。
