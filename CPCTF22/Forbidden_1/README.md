# Forbidden 1
category: Web
10.00 points, 75 solves

## 問題
> フラグはadminしか取得できないから大丈夫なはず...
> [forbidden-1.cpctf.space](https://forbidden-1.cpctf.space/)

## 解法
cookieを見るとadminがfalseになっている。これをtrueにした上で旗の画像をクリックすればよい。cookieを変えるには開発者ツールのコンソールで
```js
cookieStore.set('admin',true);
```
を実行すればよい。
