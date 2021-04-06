from flask import render_template, request , redirect, url_for, flash
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
    return render_template("discount_select.html") # actually the index page will route "discount_select"

# discount_select page
@app.route("/discount_select", methods = ['POST', 'GET'])
def discount_select():
    return render_template("discount_select.html")

# login page
@app.route("/login", methods = ['POST', 'GET'])
def login():
    if current_user.is_authenticated:   # is_authenticated return True if now have a login current_user
        return redirect(url_for('room_list'))   # TODO to check which page to direct

    if request.method == 'POST':  # if POST
        if request.form['submit'] == 'sign_in':    # if get login submit
            username = request.form.get('account') # get username
            password = request.form.get('passwd') # get password
            user = User.query.filter_by(name=username).first()  # get User Object
            if user == None:
                return redirect(url_for("login"))
            else:
                if user.password == password:   # password correct 
                    login_user(user)    # login
                    return redirect(url_for("room_list"))   # TODO to check which page to direct


        elif request.form['submit'] == 'sign_up':
            new_username = request.form.get('new_acc')
            new_password = request.form.get('new_passwd')
            user = User(new_username, new_password)
            db.session.add(user)
            db.session.commit()
            return redirect(url_for("login"))

    return render_template("login.html")

@app.route("/room_list",methods = ['POST', 'GET'])
def room_list():

    # TODO ensure if there is login logout in each navigation bar
    # if request.method == 'POST':
    #     if request.form['action'] == 'login':
    #         return redirect(url_for("login"))
    #     elif request.form['action'] == 'create':
    #         return redirect(url_for("create_room"))

    obj_R = Room.query.order_by(Room.id).all()
    data_pass = [
        {"event" :obj.event,
        "location": obj.location,
        "time":obj.time,
        "name":User.query.filter_by(id=obj.hostid).first().name,
        "rate":User.query.filter_by(id=obj.hostid).first().rate
        }
        for obj in obj_R
        ]
    return render_template("room_list.html", data = data_pass)


@app.route("/create_room",methods = ['POST', 'GET'])
def create_room():
    # if not login then redirect to login page
    if not current_user.is_authenticated:
        return redirect(url_for("login"))
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

            return redirect(url_for("room_list"))
    return render_template("create_room.html")

@app.route("/logout", methods = ['POST', 'GET'])
def logout():
    logout_user()
    return redirect(url_for("room_list"))
