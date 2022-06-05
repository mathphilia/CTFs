# phisher
category: misc  
70 points, 238 solves

## 問題
> ホモグラフ攻撃を体験してみましょう。  
> 心配しないで！相手は人間ではありません。  
> `nc phisher.quals.beginners.seccon.jp 44322`

## 解法
入力した文字列を画像化してOCRで読み取り、読み取り結果が`www.example.com`に一致した上で入力文字列の中に`www.example.com`に含まれる文字が1つも含まれなければflagがもらえる。まず、キリル文字にе(イェー),х(ハー),а(アー),р(エル),с(エス),о(オー)があるので、あとは`.mlw`の4文字に似た文字を見つければよい。`l`は`|`(U+007C VERTICAL LINE)でよいだろう。Unicode名にLATIN SMALL LETTER Mが含まれる文字を探せば`m`に似た文字が見つかる(wも同様)。今回は`ṃ`(U+1E43 LATIN SMALL LETTER M WITH DOT BELOW)と`ẇ`(U+1E87 LATIN SMALL LETTER W WITH DOT ABOVE)を用いた。`.`はUnicode名にDOTが含まれるものを探すと`․`(U+2024 ONE DOT LEADER)等が見つかる。以上から`ẇẇẇ․ехаṃр|е․соṃ`が条件に当てはまる。なお、文字によってはフォントが対応してい>ないので注意が必要。
