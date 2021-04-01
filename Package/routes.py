from flask import render_template, request ,flash, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from Package import app, db
from Package.models import User, Post


# web server

# # resolute favicon.ico problem
# import os from flask import send_from_directory  
# @app.route('/favicon.ico') 
# def favicon():     
#     return send_from_directory(os.path.join(app.root_path, 'static'),
#     'favicon.ico', mimetype='image/vnd.microsoft.icon')

# main page
@app.route("/", methods = ['POST','GET'] )
def index():
    # if the frontend use POST to backend
    if request.method == 'POST':
        return render_template("login.html")
    return render_template("index.html")


@app.route("/login", methods = ['POST', 'GET'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        user = User(username,password)
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template("login.html")
