from flask import render_template, request ,flash, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from Package import app, db
from Package.models import User, Room
from jinja2 import Template


# web server

# # resolute favicon.ico problem
# import os from flask import send_from_directory  
# @app.route('/favicon.ico') 
# def favicon():     
#     return send_from_directory(os.path.join(app.root_path, 'static'),
#     'favicon.ico', mimetype='image/vnd.microsoft.icon')

#function for transforming db_form
def trans_db(id_location):
    # list_room_id = []
    # list_room_event = []
    # for items in room_id:
    #     list_room_id.append(items)
    # for items in room_event:
    #     list_room_event.append(items)

    for dic in id_location:
        print(dic)
    for dic in id_location:
        print(dic['id'])
    for dic in id_location:
        print(dic['location'])
    for dic in id_location:
        print(dic['time'])
    # for tup in id_location:
    #     print(tup)
    # for tup in id_location:
    #     print(tup[0])
    # for tup in id_location:
    #     print(tup[1])
        


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
        return redirect(url_for("room_list"))
    return render_template("login.html")


#TODO First
@app.route("/room_list",methods = ['POST', 'GET'])
def room_list():
    obj_R = Room.query.order_by(Room.id).all()
    # name_rate=[]
    # for obj in obj_R:
    #     id = obj.hostid
    #     user = User.query.get(id).all()
    #     dic = {"name":user.name, "rate":user.rate}
    #     name_rate.append(dic)


    data_pass = [
        {"event" :obj.event,
        "location": obj.location,
        "time":obj.time,
        "name":User.query.filter_by(id=obj.hostid).first().name,
        "rate":User.query.filter_by(id=obj.hostid).first().rate
        }
        for obj in obj_R
        ]

    print(data_pass)
    return render_template("room_list.html", data = data_pass)




#TODO Second
@app.route("/create_room",methods = ['POST', 'GET'])
def create_room():
    if request.method == 'POST':
        pass
        # TODO
    
        return redirect(url_for("room_list"))
    return render_template("create_room.html")
    
