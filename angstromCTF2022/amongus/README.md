# amongus
category: Misc  
40 points, 632 solves

## 問題
> One of [these](amongus.tar.gz) is not like the others.

## 解法
添付ファイルを解凍すると大量のテキストファイルが出てくる。ほとんどのファイルの内容は同じだが1つだけ違うものがあり、そのファイルのファイル名(`.txt`を除いた部分)がflagである。Pythonでは`os`モジュールの`listdir`函数を使うと指定したディレクトリのファイル名を全て取得できる。
