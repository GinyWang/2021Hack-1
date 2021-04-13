# 2021-HackUST

## File Directory Dependency
![File Dependency](https://raw.githubusercontent.com/clsied/2021Hack/main/tree.png?token=ANGPPRX4Q6D4CP2KXZ6Z2XLAOVOTO)


## FrontEnd

### Notice
1. comment很重要
2. 顏色之後再統一，先藍色為主
3. 記得是手機的screen size
4. 4/4 當天把前三個解決，先不用丟上來，截圖有東西就好 
5. css html js file 命名好一點

### Responsiblity
1. 優惠選擇頁面 (bungee)
      -用好看一點的list呈現 (可上網找其他code直接用)  
      -[這裡](https://www.youtube.com/watch?v=fxY1q4SCB64)
2. 房間列表頁面 (jason)
      -說明：此頁面為進入某項優惠後，選擇想要加入的出遊團的房間列表
      -進度：完成html初版  
      -下一步：編寫每頁可以共用的navigation bar，待此頁需要的div都確認後開始css地獄
3. 開房頁面 (giny)
      -一般的form呈現   
      -[這裡](https://www.youtube.com/watch?v=zT62eVxShsY)
4. chatbox
      -可參考  
      -[這裡](https://www.youtube.com/watch?v=zQyrwxMPm88) 
5. 活動結束後的推薦項目頁面
      -上面的做完再說


## BackEnd

Finished:

1. Finished create_room() related
2. Finished discount_select() and continue working on button
3. Finished login() related
4. Finished room_list() and continue checking css js file and working on button

## DataBase

Finished:  

1. Finished Database Model with SQLite 
2. Dummy data created (dummy.py)  

# Summary for PPT
## Database
1. store user information  
2. access database by using flask / flask_sqlalchemy  
3. model.py construct object types for each information of our customers 

## routes.py
1. arrange website routes  
2. design functions for each webpage  
3. backend receive ```['GET', 'POST']``` method to request data from database  
4. use Query to request data from database  
5. send back data of each room_list / chatbox as dictionary type to frontend  
6. HTML demonstrate results on webpage by using jinja

## Useful Link

### Recommend Download for DataBase LookUp
[SQLite Browser](https://sqlitebrowser.org/)

## For Laibon 

1. ~~使用者的資料庫 & 優惠(貼文)的資料庫 建檔~~ (cwuan已完成)

2. ~~使用[SQLite Browser](https://sqlitebrowser.org/)連結，查看Database裡面的形式~~  (laibon已完成)

3. ~~查看前端網頁裡面的button如何跟Flask連結~~ (laibon已完成)

4. ~~了解cwuan寫的comment和新的package架構~~ (laibon已完成)

5. 學flask (laibon持續)

6. ~~參考[這個stackoverflow](https://stackoverflow.com/questions/51669102/how-to-pass-data-to-html-page-using-flask)  
和[flask tutorial](https://youtu.be/QnDWIZuWYW0)  
和[jinja語法庫](https://jinja.palletsprojects.com/en/2.11.x/)  
和[Querying Records](https://flask-sqlalchemy.palletsprojects.com/en/2.x/queries/)寫~~ 
(laibon已完成)  
7. ~~理解[靜態檔使用方式](https://mrnegativetw.github.io/Python-3-%E7%AD%86%E8%A8%98/Flask/Python3%E7%AD%86%E8%A8%98-%E7%94%A8Flask%E7%9A%84url_for%E9%80%A3%E7%B5%90%E5%88%B0static%E4%B8%AD%E7%9A%84%E5%AD%90%E8%B3%87%E6%96%99%E5%A4%BE/)  
和[Flask-Login](https://youtu.be/CSHx6eCkmv0)  
和[Flask使用者基本資料](https://youtu.be/803Ei2Sq-Zs)~~(laibon已完成)

## Requirement

```bash
pip install Flask==1.1.2
pip install python==3.7.3
pip install Flask-SQLAlchemy==2.5.1
pip install Flask-Login
```  
## License
[MIT](https://choosealicense.com/licenses/mit/)
