# whatsmyname
category: Pwn  
50 points, 296 solves

## 問題
> Can you guess my name?
> 
> `nc challs.actf.co 31223`
> 
> [whatsmyname](whatsmyname) [whatsmyname.c](whatsmyname.c)

## 解法
バッファオーバーフロー的なものを疑って48文字以上の名前を入れてみると入力した名前に加えてmyNameが出力される(微妙に原理が理解できていない)。ただしこちらの入力の冒頭48bytesがyourNameに、49bytes目(1-based)以降がguessになるので自分の名前は48bytesにしないといけない。何故か分からないが、solver.pyを実行しても2回に1回くらいはflagが手に入らない。
