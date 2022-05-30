# same old
26.0 points

## 問題
> Hack \_\_\_ planet!  
> Submit a string that complies with the following rules:  
> - The string should start with the punycode of your team name (it's __PUNYCODE OF YOUR TEAM NAME__). This is a good time for you to figure out with which team you are playing. Do not play for more than one team!
> - After your team name, you may add any number of alphanumeric characters.
> - CRC32(the\_intended\_answer) == CRC32(your\_string)

## 解法
`Hack ___ planet`で検索するとHack the planetが出てくる。よく分からないが`the_intended_answer`はtheらしい。なので、自分のチーム名(のpunycode)+英数字列の形の文字列のうちCRC32のチェックサムが"the"のCRC32チェックサムに一致するようなものがflagである。例えばチーム名が`TEAM_NAME`であれば、CRC32('the') == CRC32('TEAM\_NAME0Or1Vi')であるので`TEAM_NAME0Or1Vi`等がflagになる。CRC32の逆算は[こちらのQiitaの記事](https://qiita.com/taiyaki8926/items/94b8f12973d477749d10)を参考にして考えればよい。
