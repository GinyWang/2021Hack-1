from Package import db # from __init__ import app db Object
import os
from Package.models import User, Room

if __name__ == '__main__':
    
    # get current directory
    current_dir = os.path.abspath(os.path.dirname(__file__))
    # go to that directory
    os.chdir(current_dir+'/Package')
    # delete database and create new database
    if os.path.exists("data.sqlite"):
        os.remove("data.sqlite") 
    db.create_all()

    # User parameters
    name_list = ['Malaikah Wood','Elaina Talley','Kishan Doherty','Eddison Weston','Rhona Hensley',
    'Yassin Charles','Donald Noel','Winnie Mclean','Vivaan Vincent','Maia Whitmore',
    'Jazmin Espinosa','Mischa Lake','Natan Mills','Liya Harwood','Milena Hunt',
    'Kailum Durham','Giorgia Lutz','Aleksander Roberson','Lylah Shelton','Layla-Rose Whiteley']

    password_list = ['hack','hack','hack','hack','hack',
    'hack','hack','hack','hack','hack',
    'hack','hack','hack','hack','hack',
    'hack','hack','hack','hack','hack']



    # Room parameters   
    event_list = ['event1','event2','event3','event4','event5']

    description_list = ['description1','description2','description3','description4','description5']

    pplneed_list = [5,3,7,4,6]
    
    time_list = ['2021/04/12/3pm','2021/04/16/8pm','2021/04/14/3pm','2021/04/12/6pm','2021/04/12/5pm']

    location_list = ['Yuen Long','Kwun Tong','Tsuen Wan','Sai Kung','Kwai Tsing']

    for index in range(20):
        db.session.add(User(name_list[index],password_list[index]))
        db.session.commit()
    
    user = User.query.filter_by(name='Malaikah Wood').first()
    user.rooms.append(
        Room(event_list[0],time_list[0],location_list[0],description_list[0],pplneed_list[0],user.id)
        )

    user = User.query.filter_by(name='Winnie Mclean').first()
    user.rooms.append(
        Room(event_list[1],time_list[1],location_list[1],description_list[1],pplneed_list[1],user.id)
        )

    user = User.query.filter_by(name='Kishan Doherty').first()
    user.rooms.append(
        Room(event_list[2],time_list[2],location_list[2],description_list[2],pplneed_list[2],user.id)
        )

    user = User.query.filter_by(name='Giorgia Lutz').first()
    user.rooms.append(
        Room(event_list[3],time_list[3],location_list[3],description_list[3],pplneed_list[3],user.id)
        )

    user = User.query.filter_by(name='Rhona Hensley').first()
    user.rooms.append(
        Room(event_list[4],time_list[4],location_list[4],description_list[4],pplneed_list[4],user.id)
        )
    db.session.commit()