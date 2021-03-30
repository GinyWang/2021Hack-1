from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import os
app = Flask(__name__)

# get current directory
current_dir = os.path.abspath(os.path.dirname(__file__))

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + \
    os.path.join(current_dir, 'data.sqlite')

db = SQLAlchemy(app)


# TODO in Class
# Remember the @staticmethod later
# think which function should add
class UserModule(db.Model):

    # attribute
    # store user data -> what data need to store?
    # TODO
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True, nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(100))

    # initialization
    # when create the object
    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password

    # save to database
    def save(self):
        db.session.add(self)
        db.session.commit()
    
    # delete from database
    def delete(self):
        db.session.delete(self)
        db.session.commit()
    
    # update to database
    # first assign to attribute then call the function
    def update(self):
        db.session.commit()
    


# find by name
def find(cls, name):
    return cls.filter_by(name == name).first()

# web server
@app.route("/",methods = ['POST', 'GET'])
def index():
    if request.method == 'POST':
        name = request.form.get('username')
        email = request.form.get('email')
        password = request.form.get('password')
        User = UserModule(name,email,password)
        User.save()
    return render_template("index.html")

        
    
if __name__ == '__main__':
    if not os.path.exists('data.sqlite'):
        db.create_all()
    
    app.run(host='localhost',debug=True)
