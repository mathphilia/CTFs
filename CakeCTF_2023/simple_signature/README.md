# simple signature
category: Crypto  
105 points, 88 solves

## 問題
> It must be a piece of cake. `nc crypto.2023.cakectf.com 10444`

## 解法
署名の問題。`h("cake_does_not_eat_cat")`に適合する署名 $(s,t)$ を見つけられれば勝ちで、`"cake_does_not_eat_cat"`以外の文字列`x`であれば`h(x)`の署名を貰える。メッセージ $m$ に対する署名 $(s,t)$ は、鍵 $g,w,v$ を用いて $g^m\equiv s^wt^{-v}\pmod p$ が成り立つか否かで正当性が検証される。`h("cake_does_not_eat_cat")`を整数に変換したものを $m$ とし、適当に選んだ文字列`x`に対して`h(x)`を整数に変換したものを $m_x$ とする。また、 $m_x$ に対する署名(の1つ)を $(s_x,t_x)$ とする。このとき $g^{m_x}\equiv s_x^wt_x^{-v}\pmod p$ が成り立つが、これをうまく操作して $g^m$ を作りたい。両辺に $g^{m-m_x}$ を掛けると  

$$g^m\equiv s_x^wt_x^{-v}g^{m-m_x}=s_x^wt_x^{-v}(g^\frac{m-m_x}{-v})^{-v}=s_x^w(t_xg^\frac{m-m_x}{-v})^{-v}\pmod p$$

となる。ここで、`keygen`函数中の操作より $v$ が $\bmod p-1$ 上可逆であることに注意。以上より、 $(s_x,t_xg^\frac{m-m_x}{-v})$ は`h("cake_does_not_eat_cat")`に適合する署名である。
