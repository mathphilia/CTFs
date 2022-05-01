# the luck 1
category: Misc  
328.36 points, 18 solves

## 問題
> `nc theluck1.cpctf.space 30002`  
> the luck 1とthe luck 2は独立した問題です。

## 解説
サーバに接続すると同時に時刻を取得し、問題ファイルのプログラムと同様にC言語で疑似乱数を生成する。今回は`subprocess`モジュールを使ったが、`int(time.time())`を出力してからその値をもとに別の場所でCプログラムを動かしてもよい。
