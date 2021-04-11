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
    name_list = ['admin','admin2','Kishan','Eddison','Rhona',
    'Yassin','Donald','Winnie','Vivaan','Maia',
    'Jazmin','Mischa','Natan','Liya','Milena',
    'Kailum','Giorgia','Aleksander','Lylah','Layla-Rose']

    password_list = ['hack','hack','hack','hack','hack',
    'hack','hack','hack','hack','hack',
    'hack','hack','hack','hack','hack',
    'hack','hack','hack','hack','hack']



    # Room parameters   
    event_list = ['LKF Hotel','PizzaHutt Hotel','Diseny','Ocean Park','KFC',
    'HALL22222','Conference Lodge','McDonald','Burger King', 'SUbWAY']
    
    date_list = ['2021-05-12','2021-04-18','2021-12-01','2031-04-23','2023-04-21',
    '2023-06-01','2021-12-31','2021-05-13','2021-04-15','2021-09-01']

    time_list = ['01:21','01:32','11:12','11:41','01:12',
    '05:13','05:17','11:16','10:41','07:12']

    location_list = ['Yuen Long','Kwun Tong','Tsuen Wan','Sai Kung','Kwai Tsing',
    'Sai Kung','Kwun Tong','Yuen Long','Kwun Tong','Tsuen Wan']

    pplneed_list = [5,3,7,4,6,
    5,3,7,8,4]

    description_list = ['Come on','Go Go Go','Hey there!','SUPER!!!','LetGo',
    'SLEEP!','SLEEEEEEEP Zzzz','Come here','Go Yoloooooooo','Eaaaaatttttt',]

    type_list = ['Accommodations','Accommodations','Tickets','Tickets','Cuisines',
    'Accommodations','Accommodations','Cuisines','Cuisines','Cuisines']

    chat_list = ['1:How are you\n1:Let us sleep',
    '1:Hey there\n1:Let us gogogo',
    '4:Hi\n4:Let us have fun',
    '17:Yolooooo',
    '1:Hey there\n1:Group togther\n1:My name is admin\n1:hehe',
    '18:Yolooooo\n18:Why is it accommodation',
    '1:Yo man\n1:Typing is so boring',
    '18:YOHOLOLO\n18:Let us go eattttttt',
    '3:End',
    '2:I am admin2'
    ]

    for index in range(20):
        db.session.add(User(name_list[index],password_list[index]))
        db.session.commit()
    
    def room_input(hostname,ind):
        user = User.query.filter_by(name=hostname).first()
        user.rooms.append(
            Room(event_list[ind],date_list[ind],time_list[ind],location_list[ind],
            description_list[ind],pplneed_list[ind],type_list[ind],user.id,
            chat_list[ind])
        )

    room_input('admin',0)
    room_input('admin',1)
    room_input('Eddison',2)
    room_input('Giorgia',3)
    room_input('admin',4)
    room_input('Aleksander',5)
    room_input('admin',6)
    room_input('Aleksander',7)
    room_input('Kishan',8)
    room_input('admin2',9)
    db.session.commit()
