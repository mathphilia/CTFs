# cbc
category: Crypto  
152 points, 59 solves

## 問題
who on earth is putting CLASSICAL BORING CRYPTOGRAPHY in my ctf

## 解法
古典暗号的な操作とCBC的な操作が組み合わさっている。第 $i$ ブロックの平文を $\\texttt{plain}_i$ と書くと、第 $k$ ブロックの暗号文 $\\texttt{cipher}_k$ は  
$$\\texttt{cipher}_k=\\texttt{iv}+\\texttt{plain}_0+\\texttt{plain}_1+\\dots+\\texttt{plain}_k+k\\cdot\\texttt{key}$$  
である。ただし、 $+$ は`add_key`函数で行われる演算であり、 $k\\cdot\\texttt{key}=\\texttt{key}+\\texttt{key}+\\dots+\\texttt{key}$ ( $\\texttt{key}$ が $k$ 個)である。よって次の式が得られる。  
$$\\texttt{cipher}_0-\\texttt{iv}=\\texttt{plain}_0+\\texttt{key}$$  
$$\\texttt{cipher}_k-\\texttt{cipher}_{k-1}=\\texttt{plain}_k+\\texttt{key} (1\\leqq k)$$  
ここで`add_key`函数で行われる演算がVigenère暗号であることに気づけば、[このウェブサイト](https://www.dcode.fr/vigenere-cipher)等を使うことにより解くことができる。なおこのウェブサイトでは最大500文字までしかデコードできないようなので、鍵だけもらって後のデコードは自力で行うこととする。以上でメッセージが得られるが、すべて大文字で分かち書きもされていないので読みづらい。[これ](https://quipqiup.com/)は換字式暗号の解読ツールだが、ついでに分かち書きもしてくれる。最後の方を読むと  
> ... anyway here comes the flag its everything after this at least its not a generic rot thirteen challenge i guess  
と書いてある。どこからflagなのか分かりづらいが、`corCTF{ATLEASTITSNOTAGENERICROTTHIRTEENCHALLENGEIGUESS}`が正解。
