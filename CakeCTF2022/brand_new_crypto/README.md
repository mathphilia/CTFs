# brand new crypto
category: Crypto
140 points, 46 solves

## 問題
> One day, I came up with a brand-new idea.

## 解法
公開鍵は$(s,t,n)$であり、平文$m$に対する暗号文は乱数$r$を用いて$(c_1,c_2)=(mr^s\bmod n,mr^t\bmod n)$と書ける。ここで、$c_1^tc_2^{-s}\bmod n=m^{t-s}\bmod n$であるから、RSA暗号に帰着できる。$m$は$1,2,3,\dots,255$の$255$通りの値しか取り得ないので、$m^{t-s}\bmod n$から$m$が求まる。
