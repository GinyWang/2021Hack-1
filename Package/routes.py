from flask import render_template, request ,flash, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from Package import app, db
from Package.models import User, Room

# main page
@app.route("/", methods = ['POST','GET'] )
def index():
    # if the frontend use room to backend
    if request.method == 'POST':
        return render_template("login.html")
    return render_template("index.html")


@app.route("/login", methods = ['POST', 'GET'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        return redirect(url_for("create_room"))
    return render_template("login.html")

@app.route("/room_list",methods = ['POST', 'GET'])
def room_list():
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
    if request.method == 'POST':
        if request.form['submit'] == 'Submit':
            event = request.form.get('Ename')
            time = request.form.get('Etime')
            location = request.form.get('ELoc')
            pplneed = request.form.get('NumPeople')
            description = request.form.get('descrip')
            
            # dummy poster
            room = Room(event,time,location,description,pplneed,1)
            db.session.add(room)
            db.session.commit()
            return redirect(url_for("room_list"))

        elif request.form['reset'] == 'Reset':
            return render_template("create_room.html")

    return render_template("create_room.html")
