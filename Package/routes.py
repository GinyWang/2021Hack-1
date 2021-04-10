from flask import render_template, request , redirect, url_for, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_login import login_user, current_user, logout_user
from Package import app, db
from Package.models import User, Room

# TODO
# test logout function by login again
# test create room to ensure new one is login


# index page
@app.route("/", methods = ['POST', 'GET'])
def index():
    return redirect(url_for('login_out')) # actually the index page will route "login_out"

# discount_select page
@app.route("/discount_select", methods = ['POST', 'GET'])
def discount_select():
    return render_template("discount_select.html")

# login page
@app.route("/login_out", methods = ['POST', 'GET'])
def login_out():
    # if current_user.is_authenticated:   # is_authenticated return True if now have a login current_user
    #     logout_user()
    #     return redirect(url_for('discount_select'))   # TODO to check which page to direct
    if request.method == 'POST':  # if POST
        if request.form['submit'] == 'sign_in':    # if get login submit
            username = request.form.get('account') # get username
            password = request.form.get('passwd') # get password
            user = User.query.filter_by(name=username).first()  # get User Object
            if user == None:
                return redirect(url_for("login_out"))
            else:
                if user.password == password:   # password correct 
                    login_user(user)    # login
                    return redirect(url_for("discount_select"))   # TODO to check which page to direct


        elif request.form['submit'] == 'sign_up':
            new_username = request.form.get('new_acc')
            new_password = request.form.get('new_passwd')
            user = User(new_username, new_password)
            db.session.add(user)
            db.session.commit()
            return redirect(url_for("login_out"))

    return render_template("login.html")

@app.route("/room_list", defaults = {'distype':''}, methods = ['POST', 'GET'])
@app.route("/room_list/<distype>", methods = ['POST', 'GET'])
def room_list(distype):
    
    Room_list = []
    if request.method == 'POST':
        if request.form.get('type'):
            Room_list = Room.query.filter_by(distype = request.form['type']).all()
        
            
        # room id
        if request.form.get('join'):
            identity = request.form.get('join')
            room = Room.query.filter_by(id=identity).first()
            room.pplnow += 1
            current_user.rooms.append(room)
            db.session.commit()

            return redirect(url_for('chatbox',roomid=identity))
    if len(distype) :
        Room_list = Room.query.filter_by(distype = distype).all()
    if not len(Room_list) :
        Room_list = Room.query.all()
    
    data = [
        {"event" : room.event,
        "date": room.date,
        "time": room.time,
        "location": room.location,
        "pplnow": room.pplnow,
        "pplneed": room.pplneed,
        "hostname": User.query.filter_by(id = room.hostid).first().name,
        "hostrate": User.query.filter_by(id = room.hostid).first().rate,
        "id" : room.id
        }
        for room in Room_list
    ]
    
    return render_template("room_list.html", data = data)
    


@app.route("/create_room", methods = ['POST', 'GET'])
def create_room():
    # if not login then redirect to login page
    if not current_user.is_authenticated:
        return redirect(url_for("login_out"))

    if request.method == 'POST':
        if request.form['submit'] == 'Submit':
            event = request.form.get('EvName')
            date = request.form.get('EvDate')
            time = request.form.get('EvTime')
            distype = request.form.get('EvType')
            location = request.form.get('EvLoc')
            pplneed = request.form.get('NumPeople')
            description = request.form.get('EvDescr')
            room = Room(event,date,time,location,description,pplneed,distype,current_user.id)
            current_user.rooms.append(room)
            db.session.commit()

            return redirect(url_for("room_list", distype = distype))
    return render_template("create_room.html")

@app.route("/chatbox", defaults = {'roomid':''}, methods = ['POST', 'GET'])
@app.route("/chatbox/<roomid>", methods = ['POST', 'GET'])
def chatbox(roomid):

    print(roomid)
    room = Room.query.filter_by(id = roomid).first()
    raw_chat = room.chat
    if raw_chat != None:
        split_chat = raw_chat.split("\n")
    else:
        split_chat = raw_chat
    data = []
    if split_chat != None:
        for chat in split_chat:
            idx = chat.find(':',)
            chat_id = int(chat[:idx])
            is_mychat = False
            if chat_id == current_user.id:
                is_mychat = True
            chat_content = chat[idx+1:]
            data.append((is_mychat,chat_content))
    
    if request.method == 'POST':
        chat = request.form['chat']
        if raw_chat == None:
            room.chat = str(current_user.id) + ":" + chat
        else:
            room.chat = raw_chat + '\n' +str(current_user.id) + ":" + chat
        db.session.commit() 
        return jsonify()

    return render_template("chatbox.html", data = data, event = room.event, identity = room.id)

@app.route("/room_record", methods = ['POST', 'GET'])
def room_record():

    if not current_user.is_authenticated:
        return redirect(url_for('login_out'))

    if request.method == 'POST':
        identity = request.form.get('enter')
        return redirect(url_for('chatbox',roomid = identity))
    
    Room_list = []
    Room_list = current_user.rooms

    data = [
        {"event" : room.event,
        "date": room.date,
        "time": room.time,
        "location": room.location,
        "pplnow": room.pplnow,
        "pplneed": room.pplneed,
        "hostname": User.query.filter_by(id = room.hostid).first().name,
        "hostrate": User.query.filter_by(id = room.hostid).first().rate,
        "id" : room.id
        }
        for room in Room_list
    ]      
    # if not len(Room_list):
    #     data = [
    #     {"event" : "N/A",
    #     "date": "N/A",
    #     "time": "N/A",
    #     "location": "N/A",
    #     "pplnow": "N/A",
    #     "pplneed": "N/A",
    #     "hostname": "N/A",
    #     "hostrate": "N/A",
    #     "id" : "N/A"
    #     }
    # ]
    
    return render_template("room_record.html",data = data)
