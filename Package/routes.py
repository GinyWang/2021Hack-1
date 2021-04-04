from flask import render_template, request ,flash, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_login import login_user, current_user
from Package import app, db
from Package.models import User, Room

# main page

@app.route("/", methods = ['POST', 'GET'])
def index():
    return redirect(url_for("room_list"))


@app.route("/login", methods = ['POST', 'GET'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('room_list'))
    if request.method == 'POST':

        username = request.form.get('username')
        password = request.form.get('password')

        user = User.query.filter_by(name=username).first()
        if user.password == password:
            login_user(user)
        
            return redirect(url_for("room_list"))
    return render_template("login.html")

@app.route("/room_list",methods = ['POST', 'GET'])
def room_list():
    
    if request.method == 'POST':
        if request.form['action'] == 'login':
            return redirect(url_for("login"))
        elif request.form['action'] == 'create':
            return redirect(url_for("create_room"))

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
            event = request.form.get('Ename')
            time = request.form.get('Etime')
            location = request.form.get('ELoc')
            pplneed = request.form.get('NumPeople')
            description = request.form.get('descrip')
            
            # dummy poster
            room = Room(event,time,location,description,pplneed,current_user.id)
            current_user.rooms.append(room)
            db.session.commit()
            return redirect(url_for("room_list"))
    return render_template("create_room.html")

@app.route("/logout", methods = ['POST', 'GET'])
def logout():
    logout_user()
    return redirect(url_for("room_list"))
