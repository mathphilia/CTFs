# Command
category: Crypto  
106 points, 88 solves

## 問題
> 安全なコマンドだけが使えます  
> `nc command.quals.beginners.seccon.jp 5555`

## 解法
メニューの1を選ぶと`b'fizzbuzz'`および`b'primes'`をAES-CBCで暗号化したものとIV(初期化ベクトル)がもらえる。また、メニューの2を選ぶと入力をAES-CBCで復号したものに対応したコマンドが実行される。ここで`b'getflag'`を渡すことができればflagが得られる。重要なのは、2のときにIVをこちら側で任意に指定できるという点である。PKCS #7によるパディングを`pad`, AESの暗号化函数を`encrypt`とおけば、16bytes以下の`input`をAES-CBCで暗号化するとencrypt(pad(input) xor IV)となる。よって、メニュー1で`b'fizzbuzz'`を暗号化した際のIVをIV<sub>0</sub>とおけばencrypt(pad(b'getflag') xor (IV<sub>0</sub> xor pad(b'fizzbuzz') xor pad(b'getflag')))はencrypt(pad(b'fizzbuzz') xor IV<sub>0</sub>)に一致する。
