# ding-dong-ting-ping
category: Crypto  
220 points, 17 solves

## 問題
> `nc crypto.2023.cakectf.com 11111`

## 解法
cookieがCBCに似たスキームの暗号で暗号化されている。前のブロックの暗号文と今のブロックの平文を単にxorしてから暗号化するのではなく、前のブロックの暗号文のMD5ハッシュ xor 今のブロックの平文を暗号化する。まずはPREFIXの桁数を探るためにusernameを変えていく。すると`aaaaaaaaa`と`aaaaaaaax`では暗号文の3ブロック目が異なるが`aaaaaaaaaa`と`aaaaaaaaax`では暗号文の3ブロック目が一致する。暗号文の第1ブロックはIVであるのでPREFIXは17桁あることになる。  

```
                 -----PREFIX----- -|user=aaaaaaaax |2023-xx-xx xx:x x:xx.xxxxxx 
-------IV------- -------a1------- -------a2------- -------a3------- -------a4-------

                 -----PREFIX----- -|user=aaaaaaaaa x|2023-xx-xx xx: xx:xx.xxxxxx 
-------IV------- -------b1------- -------b2------- -------b3------- -------b4-------
```

usernameをrootにしたいので次のような平文に対応する暗号文を作ることを目指す(時刻はチェックされないので適当でいい)。  

```
                 -----PREFIX----- -|user=root|
-------IV------- -------c1------- -------c2-------
```

適当なusernameを設定したときの暗号文の形を考えてみる。

```
                 -----PREFIX----- -|user=123456789 ------hoge------ |2023-xx-xx xx:x x:xx.xxxxxx
-------IV------- -------d1------- -------d2------- -------d3------- -------d4------- -------d5-------
```

`c2`=`d3`となるような`hoge`を求めよう。MD5(`c1`) xor `-|user=root|\x04\x04\x04\x04`=MD5(`d2`) xor `hoge`であればよく`c1`=`d1`なので、`hoge`=`-|user=root|\x04\x04\x04\x04` xor MD5(`d1`) xor MD5(`d2`)とすればよい。ここで、`-|user=root|\x04\x04\x04\x04`の最初の1byteはPREFIXの最終byteなので未知だが、256通り全探索すればよい。
