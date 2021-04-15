## File Dependecy
![GitHub](https://raw.githubusercontent.com/clsied/2021Hack/main/tree.png?token=ATCR6EJEBTG7ORKBKZYU5D3AP7HU2 "tree")  
  
  
## Prerequisites
```
pip install Flask==1.1.2
pip install python==3.7.3
pip install Flask-SQLAlchemy==2.5.1
pip install Flask-Login
```
  
## License  
[MIT](https://choosealicense.com/licenses/mit/)  
  
## Useful Link  
### Recommend Download for DataBase LookUp  
[SQLite Browser](https://sqlitebrowser.org/)
  
## Introduction  
#### Initiate database
+ dummy.py => create database
+ app.py => initiate our program( url generated )  
+ click the url generated in the terminal  
#### Login  
+ login.html send form to backend for verifying purpose
+ routes.py access to backend and exam if is valid account  
  => if not, create account  
#### Navigation Bar  
+ you can find every webpage you might need  
#### Create room    
+ fill up blank for room information  
+ create_room.html send information to backend  
+ routes.py save information into database for further usage
+ number of people in the room +1  
#### Join the Room  
+ click JOIN button to enter the room you are interested in  
+ room_list.html send form back to routes.py with specific room id  
+ leave the room by clicking the white arrow button and return to the main room list  
#### Chat  
+ send your message by clicking the send button  
+ chatbox.html send a form with specific room id to routes.py  
+ backend save the chat record into database  
#### log out  
+ find log out button in navigation bar  
