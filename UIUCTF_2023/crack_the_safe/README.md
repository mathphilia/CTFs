# crack\_the\_safe
category: Crypto  
69 points, 62 solves

## 問題
> "I found this safe, but something about it seems a bit off - can you crack it?"

## 解法
AES-ECBの暗号化鍵`key`に対し、 $7^\texttt{key}\bmod p$ が与えられている。この値を $y$ とおく。 $p$ は $192$ bitなので`key`は $192$ bit以下であろうと考えられる。AESの暗号化鍵のサイズは $128$ bit, $192$ bit, $256$ bitの $3$ 種類があるが、[Group Project](https://github.com/mathphilia/CTFs/tree/main/UIUCTF_2023/Group_Project)の鍵長が $128$ bitであったことから今回もそうなのではという希望的観測の下で解いていく。 $p-1$ を素因数分解すると

$$p-1=2\times19\times151\times577\times67061\times18279232319\times111543376699\times9213409941746658353293481$$

であり、 $q=9213409941746658353293481$ 以外の素因数はそこまで大きくない。離散対数問題 $7^x\bmod p=y^{9213409941746658353293481}$ を[Discrete logarithm calculator](https://www.alpertron.com.ar/DILOG.HTM)で解いてもらうと解

$$x\equiv444780066250058017668829040430952\times9213409941746658353293481\pmod{p-1}$$

が得られる。 $x_0=444780066250058017668829040430952$ とおくと $\texttt{key}=x_0+k\dfrac{p-1}q$ なる $k$ が存在することになる。 $\texttt{key}$ は $128$ bit程度、 $\dfrac{p-1}q$ は $109$ bitであるから、 $k$ の探索範囲の大きさは $2^{19}$ 程度であり、現実的な時間で計算が完了する。
