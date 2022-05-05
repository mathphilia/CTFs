# Confetti
category: Misc
40 points, 375 solves

## 問題
> "From the sky, drop like confetti All eyes on me, so V.I.P All of my dreams, from the sky, drop like confetti" - Little Mix [confetti.png](confetti.png)

## 解法
添付された画像ファイルを`strings`にかけてみると大量に出てくるので`strings confetti.png | grep actf`してみるが何も出てこない。ここで気まぐれに`strings confetti.png | grep IEND`してみたところ、IENDが4つ出力された。1つのPNGファイルにIENDチャンクは１つしかないはずなのでこれはおかしい。もしかして４つの画像ファイルのバイナリを連結したものなのかな？と思い`b'IEND'`の周辺を見てみると

```
...\x00\x00IEND\xaeB`\x82\x89PNG\r\n\x1a\n\x00\x00\x00\rIHDR\x00\x00...
```

が見つかるのでビンゴ。あとは与えられた画像を４つに分解すると3枚目の画像にflagが書かれている。
