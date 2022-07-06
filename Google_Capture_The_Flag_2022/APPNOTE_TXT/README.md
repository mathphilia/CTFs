# APPNOTE.TXT
category: Misc
50 points, 210 solves

## 問題
> Every single archive manager unpacks this to a different file...

## 解法
普通に解凍してもhello.txtという要らんファイルしか出ないので[仕様書](http://www.idea2ic.com/File_Formats/ZIP%20File%20Format%20Specification.pdf)や[このページ](https://gist.github.com/ysakasin/2edf8d3bf55c6ebf63f82851e302b030)を参考にしてZIPファイルを読む。すると、ファイルの情報を格納するlocal file headerが大量に見つかる。また、central directoryとend of central directory record(長いので以下ECDRと略す)がたくさんという異常事態にも気づくだろう。central directoryは通常1つであるはずだが、なぜか各local file headerの直後に1つずつある。ECDRはlocal file headerほど多くあるわけではないが、通常は1つなので異常なことに変わりはない。さて、ECDRにはcentral directoryの位置を指し示す情報がある。これにより各ECDRはあるcentral directoryと結びついている。各central directoryは直前のlocal file headerと対応しているのでECDRとlocal file headerに(1対1でない)対応が作れ、格納されているファイル内容を1つずつ取り出す(圧縮されていないので簡単に読める)とflagが得られる。
