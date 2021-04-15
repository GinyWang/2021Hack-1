# Installations
  
Simply ```pip install [package_name]``` without version if package can not be installed with version specified.

``` bash
pip install Flask==1.1.2
pip install python==3.7.3
pip install Flask-SQLAlchemy==2.5.1
pip install Flask-Login==0.5.0
```

# Introduction 
 
### Initiate database
+ We recommend [DB Browser for SQLite](https://sqlitebrowser.org/) for database lookup  

+ First you can run ```dummy.py``` to initiate database and add data
+ After adding data, you may run ```app.py``` to initiate local server
+ Then click the URL generated in the terminal ```http://localhost:5000```


### Login page

+ The main route should be ```login.html``` 
+ ***At here, we suggest you login with username ```admin``` and password ```hack```***
+ You may also sign up new user by pressing ```sign-up``` button
+ After user-info submission, your submission will be checked for validation purpose


### Navigation bar  

+ ```Room joined``` webpage for login user to access previous record
+ ```Discount``` webpage for user to access different type of discount
+ ```Log in/ log out``` webpage for user to either sign in or sign out purpose


### Discount page

+ In this page we display different discount type
+ After choosing preference, the page will direct you to according discount type page


### Create room page
   
+ User can post event information and system will assign room space for the event
+ The filled-in information (room) will store in database and ***add in user's record***
 

### Join room page  
+ User may simply click ```Join``` button to enter the room that are interested in  
+ After clicking ```Join``` button, user will be redirected to chat room of joined room
+ ***User joined room will also be record and can be access in Joined record page*** 


### Chat room page  
+ We provide past chat record for users
+ User may send his message ***by clicking the ```send``` icon***
+ User may leave the room by clicking the ```white arrow ``` icon and return to the previous discount room list   


### Joined record page
+ The page is similar to Join room page
+ ***User is able to rejoin the chat room by clicking ```enter``` button***

# Open Source
+ Font-Awesome 4.7.0
+ Google Fonts
+ Bootstrap 4.0.0
+ jQuery 3.5.1
+ Popper JS 1.16.0
+ Font-Awesome 5.15.3
+ Bootstrap 4.5.2

# License                                                        
[Apache License Version 2.0, January 2004](http://www.apache.org/licenses/)  
  
