# 2021-HackUST

## Notice & TODO


HTML全部丟在templates裡面  

## For Laibon 

1. ~~使用者的資料庫 & 優惠(貼文)的資料庫 建檔~~ (cwuan已完成)

2. ~~使用[SQLite Browser](https://sqlitebrowser.org/)連結，查看Database裡面的形式~~  (laibon已完成)

3. ~~查看前端網頁裡面的button如何跟Flask連結~~ (laibon已完成)

4. ~~了解cwuan寫的comment和新的package架構~~ (laibon已完成)

5. ~~學flask~~(先跳，先看第6點)

6. 參考[這個stackoverflow](https://stackoverflow.com/questions/51669102/how-to-pass-data-to-html-page-using-flask)和[這個flask tutorial](https://www.youtube.com/watch?v=QnDWIZuWYW0&list=PL-osiE80TeTs4UjLw5MM6OjgkjFeUxCYH&index=2&ab_channel=CoreySchafer)和[這個jinja語法庫](https://jinja.palletsprojects.com/en/2.11.x/)和[這個裡面的Querying Records](https://flask-sqlalchemy.palletsprojects.com/en/2.x/queries/)寫
```bash
@app.route("/room_list",methods = ['POST', 'GET'])

#TODO
def room_list():
    pass

    return render_template("room_list.html")
```
和改寫
```html
    <div class="grid-container">
        <div class="grid-item">
            <div class="title">Let's have some fun in subway!</div>
            <div class="date">2021 April 23 16:00</div>
            <div class="host">Host By: Philip Lai</div>
            <div class="rate">Host Rate: 1 star</div>
            <button type="button" class="join btn-primary">Join</button>
        </div>
    </div>
```
成類似
```html
{% for user in users %}
  <li><a href="{{ user.url }}">{{ user.username }}</a></li>
{% endfor %}
```

## For Laibon 的整理 這是濃縮 認真看 不然我一定扁你 

### 1.為何要寫成package(套件)而不是module(模組)  

module(模組):  

將很多function分開成a.py b.py c.py，主程式app.py直接引用其函式  

package(套件):  

就是一個容器(資料夾)，包含了多個模組 (舉例我們這裡包括後端、資料庫的模組) 

並且擁有__init__.py檔案 (此檔案可以當成套件核心，主程式app.py用來直接引用，並藉由__init__.py間接使用模組)  

![示意圖](https://miro.medium.com/max/301/1*baq1t0g9N4tKXBB8nfJ2KQ.png)

### 2.Flask重點  

```bash
@app.route("/index", methods = ['POST','GET'] )
```  

主路徑 http://localhost:5000  
http://localhost:5000 + 引號裡面 = 網址  
http://localhost:5000 + index = http://localhost:5000/index

methods  
接受前端用哪些方法向後端索取資料


```bash
render_template("index.html") 
``` 
跳轉至index.html  


```bash
request.form.get('password')
  
<input type='text' name='password'>  
```
獲取 name = 'password'裡的值  


```bash
redirect(url_for('index'))
```
url_for('index')為獲取 http://localhost:5000 + index 的地址  
redirect()重新連結至此網站

### 3.Database model relationship (Many-to-Many)  

舉例說今天有兩種Data，學生和課程  

一對多: 一個學生選了多門課  
一對一: 一個學生選了一門課  
多對一: 多個學生選了同門課  
多對多: 多個學生選了多門課  

多對多的意義就在，學生可以知道他修了什麼課，相對的該門課也可以知道有哪些學生修了這門課，我們可以藉由一個學生上的其中一門課，找到一樣上這門課的其他學生

![示意圖](https://upload.wikimedia.org/wikipedia/commons/thumb/0/02/Databases-ManyToManyWJunction.jpg/1200px-Databases-ManyToManyWJunction.jpg)


### 4.Laibon的延伸資料
[Flask tutorial Part1-6](https://www.youtube.com/watch?v=MwZwr5Tvyxo&list=PL-osiE80TeTs4UjLw5MM6OjgkjFeUxCYH&index=1)  

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

## Useful Link
### Recommend Download for DataBase LookUp
[SQLite Browser](https://sqlitebrowser.org/)


## Requirement

```bash
pip install Flask==1.1.2
pip install python==3.7.3
pip install Flask-SQLAlchemy==2.5.1
```  
## File Dependency and Tree Chart

│  app.py  
│  dummy.py  
│  
├─.vscode  
│      settings.json  
│  
├─Package  
│  │  data.sqlite  
│  │  models.py  
│  │  routes.py  
│  │  __init__.py  
│  │  
│  ├─templates  
│  │      create_room.html  
│  │      index.html  
│  │      login.html  
│  │      room_list.html  
│  │      script.js  
│  │  
│  └─__pycache__  
│  
└─static  
## License
[MIT](https://choosealicense.com/licenses/mit/)
