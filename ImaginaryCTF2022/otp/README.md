# otp
category: Crypto
316 points, 48 solves

## 問題
> Encrypt your messages with our new OTP service. Your messages will never again be readable to anyone.  
>   
> `nc otp.chal.imaginaryctf.org 1337`

## 解法
secureRand函数中のjumblerは$k^n\;(k=2,3,4,\dots,9,n=0,1,2,\dots,299)$で表される整数のリストである。stateが変化していき、jumbler[state]を10進表記したときの最上位の数字が0~4なら1を、5~9なら0を追加する、ということがbitsビット集まるまで行われる。Benfordの法則より、最上位の数字が0~4である確率は5~9である確率よりそこそこ大きい(具体的には0~4: 69.875%, 5~9: 30.125%)ので、flagを何度も暗号化してもらって各ビットに0が多いか1が多いかを見ればよい。なお、secureRand函数の出力の最上位ビットは接続時に設定されるseedの値により決定されるため、1が多くならないこともよくある。
