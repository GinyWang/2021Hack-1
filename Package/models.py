from Package import db,login_manager
from sqlalchemy.orm import relationship
from sqlalchemy import ForeignKey
from flask_login import UserMixin

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))
# User room Assocation Table
# https://docs.sqlalchemy.org/en/14/orm/basic_relationships.html#many-to-many
 
user_room = db.Table('user_room',
    db.Column('room_id', db.Integer, db.ForeignKey('room.id'),primary_key=True),
    db.Column('user_id', db.Integer, db.ForeignKey('user.id'),primary_key=True)
)

# Model of User
class User(db.Model,UserMixin):

    # Object User's attribute #
    id = db.Column(db.Integer, primary_key=True)    # unique id for the Object User
    name = db.Column(db.String(100), unique=True, nullable=False)   # unique name for the Object User, not be blank
    password = db.Column(db.String(100),nullable=False) # non-unique password for the Object User
    rate = db.Column(db.Integer,nullable=False) # non-unique number of rating of this Object User
    roomnum = db.Column(db.Integer,nullable=False) # non-unique number of room-created by this Object User
    rooms = db.relationship('Room',secondary=user_room,lazy='subquery',
        backref=db.backref('users', lazy=True))

    # initialization
    def __init__(self, name, password):
        self.name = name    # create Object User with name intialized
        self.password = password    # create Object User with name intialized
        self.rate = 0   # default Object User rating
        self.roomnum = 0    # default Object User room-created number

    
# Model of room
class Room(db.Model):

    # Object User's attribute #
    id = db.Column(db.Integer, primary_key = True)    # unique id for the Object Room
    event = db.Column(db.String(100), nullable = False)   # non-unique event for the Object Room
    date = db.Column(db.String(100), nullable = False)  # non-unique event date for the Object Room
    time = db.Column(db.String(100), nullable = False)  # non-unique event time for the Object Room
    location = db.Column(db.String(100), nullable = False) # non-unique event place for the Object Room
    description = db.Column(db.Text, nullable = False)    # non-unique description for the Object Room
    pplneed = db.Column(db.Integer, nullable = False)   # non-unique number of people needed for the Object Room, constant
    pplnow = db.Column(db.Integer, nullable = False)    # non-unique number of people now in the Object Room
    distype = db.Column(db.String(100), nullable = False)   # non-unique type of discount now in the Object Room
    hostid = db.Column(db.Integer,nullable = False)   # non-unique id of host of the Object Room
    isfull = db.Column(db.Boolean, nullable = False)    # non-unique isfull of the Object Room
    # initialization
    def __init__(self,event,date,time,location,description,pplneed,distype,hostid):
        self.event = event  # create Object Room with event intialized
        self.date = date    # create Object Room with event date intialized
        self.time = time    # create Object Room with event time intialized
        self.location = location    # create Object Room with event location initialized
        self.description = description  # create Object Room with description intialized
        self.pplneed = pplneed  # create Object rRoom with people needed intialized
        self.pplnow = 1 # default number of people now in Object Room
        self.distype = distype  # create Object Room with discount type intialized
        self.hostid = hostid # create Object Room with people needed intialized
        self.isfull = False # default Boolean of iffull in Object Room

        # increment 1 to host's roomnum
        User.query.get(self.hostid).roomnum += 1    # notice that at here we dont need to db.session.commit()
                                                    # since it will db.session.commit() after the Object Room is created
                                                    # in dummy.py 
