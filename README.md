# 2021-HackUST

## Notice & TODO


HTML全部丟在templates裡面  

## For Laibon 

1. ~~使用者的資料庫 & 優惠(貼文)的資料庫 建檔~~ (cwuan已完成)

2. ~~使用[SQLite Browser](https://sqlitebrowser.org/)連結，查看Database裡面的形式~~  (laibon已完成)

3. ~~查看前端網頁裡面的button如何跟Flask連結~~ (laibon已完成)

4. ~~了解cwuan寫的comment和新的package架構~~ (laibon已完成)

5. 學flask

6. ~~參考[這個stackoverflow](https://stackoverflow.com/questions/51669102/how-to-pass-data-to-html-page-using-flask)  
和[flask tutorial](https://youtu.be/QnDWIZuWYW0)  
和[jinja語法庫](https://jinja.palletsprojects.com/en/2.11.x/)  
和[Querying Records](https://flask-sqlalchemy.palletsprojects.com/en/2.x/queries/)寫~~ 
(laibon已完成)  
7. 理解[靜態檔使用方式](https://mrnegativetw.github.io/Python-3-%E7%AD%86%E8%A8%98/Flask/Python3%E7%AD%86%E8%A8%98-%E7%94%A8Flask%E7%9A%84url_for%E9%80%A3%E7%B5%90%E5%88%B0static%E4%B8%AD%E7%9A%84%E5%AD%90%E8%B3%87%E6%96%99%E5%A4%BE/)  
和[Flask-Login](https://youtu.be/CSHx6eCkmv0)  
和[Flask使用者基本資料](https://youtu.be/803Ei2Sq-Zs)


## FrontEnd

**comment（很重要）**

顏色之後再統一，先藍色為主

記得是手機的screen size

4/4 當天把前三個解決，先不用丟上來，截圖有東西就好 

css html js file 命名好一點

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

Progress:  

2021/03/25
1. Connect Database with Flask (app.py)
2. Sample webpage for Flask testing (~~sampel.html~~ deleted)  
3. Build Server (app.py)  

2021/03/30
1. Finished Frontend to Backend to Database Code for Laibon

2021/04/01
1. Reformat Backend and Database Structure (Module format to Package format)

2021/04/03
1. Flask route to room_list create_room  
2. Finished Post in database display  

2021/04/04
1. Finished Login Logout Function

## DataBase


Progress:  

2021/03/25
1. Finished Database Model with SQLite (app.py)  
2. Connect Database with Flask (app.py)

2021/03/30
1. Finished Frontend to Backend to Database Code for Laibon

2021/04/01
1. Reformat Backend and Database Structure (Module format to Package format)
2. Database extends to User (db.Model) and Post (db.Model), many to many relationship   

2021/04/03  
1. Database stored columns(label) update  
2. Dummy data created (dummy.py)  
3. Re name Model (Post to Room)  
4. Re inherit to double class

## Useful Link
### Recommend Download for DataBase LookUp
[SQLite Browser](https://sqlitebrowser.org/)


## Requirement

```bash
pip install Flask==1.1.2
pip install python==3.7.3
pip install Flask-SQLAlchemy==2.5.1
pip install Flask-Login
```  
## File Dependency and Tree Chart

## License
[MIT](https://choosealicense.com/licenses/mit/)
