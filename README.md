# **AI_Sudoku**
数独(ナンプレ)の問題を自動生成するアプリを作成中。
処理はpython、GUIはC#で作成中。

### *現状*
---
　pythonで、解答を自動生成するところまで完成。
GUIの作成中である。GUI完成後に、問題作成(解答から何カ所か空欄を作る)に取りかかる予定である。

setp1
解答の自動生成
* *画面*
<img width="240" alt="画像の読み込み失敗" src='./demo/images/sample01.png'>
<br>

### *MENU*
---
　どんなメッセージでも良いので送信をすると、MENU画面が表示されます。使用したいモードをタップして下さい。また、各モードを途中で中断したい時は、スタンンプを送信して下さい。MENU画面に戻ります。
* *画面*
<img width="1440" alt="画像の読み込み失敗" src='./demo/images/0demo/menu1.jpg'>
<br>

### *天気モード*
---
　MENU画面の「天気モード」をタップすると、開始されます。日本各地の今日と明日の天気を表示できます。
* *画面*
<img width="1440" alt="画像の読み込み失敗" src='./app/0images/0demo/weather1.jpg'>
<br>
<img width="1440" alt="画像の読み込み失敗" src='./app/0images/0demo/weather2.jpg'>
<br>

### *オウム返しモード*
---
　MENU画面の「オウム返しモード」をタップすると、開始されます。LINE-BOTがオウム返しします。終了するには、「また明日」とメッセージを送信して下さい。
* *画面*
<img width="1440" alt="画像の読み込み失敗" src='./app/0images/0demo/echo1.jpg'>
<br>

### *注意点*
---
　スマートフォンのみ対応です。LINEアプリの仕様のため。
<br>

### *開発環境*
---
* Ruby 2.5.1
* LINE-BOT
* LINE Developer
* Github
* デプロイ HEROKU

<br>

### *今後の展開*
---
- [ ] 天気モードで一度地域登録すると、2回目以降は地域選択不要
- [ ] 明日、雨が降る場合、事前通知

などを実装していきたいと思います。

<br>

### *製作者*
---
onikunai  
Github: https://github.com/onikunai  


