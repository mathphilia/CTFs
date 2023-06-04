# polyglot4b
category: Misc  
91 points, 125 solves

## 問題
> polyglotってなに？ たぶんpolyglotを作れるエディタを開発したよ！ 
>  
> `nc polyglot4b.beginners.seccon.games 31416`

## 解法
`file -bkr [ファイル名]`の出力に`JPEG`, `PNG`, `GIF`, `ASCII`の全てが含まれるようなファイルを作る問題。とりあえず適当なJPEGファイルやPNGファイルを`file`コマンドに通してみる。添付ファイルに入っていたsushi.jpgをfileコマンドにかけると

```
JPEG image data, Exif standard: [TIFF image data, big-endian, direntries=4, description=CTF4B], baseline, precision 8, 1404x790, components 3
- data
```

と出る。Exifが出力されていることに気づく。したがってExifを編集し、`PNG GIF ASCII`とでも書き込めばよい。Exifの編集方法は[このサイト](https://www.minihack-lab.com/posts/how-to-edit-exif/)等が参考になる。なおsolver.jpgには10個以上の改行文字が含まれるが、fileコマンドは画像をパースするわけでないのでファイルの冒頭部分だけでもJPEGと認識してくれる。
