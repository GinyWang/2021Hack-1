from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
import os

app = Flask(__name__)


# get current directory
current_dir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
# configurate the database URI
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + \
    os.path.join(current_dir, 'data.sqlite')
db = SQLAlchemy(app)

app.secret_key = 'hackust2021'

login_manager = LoginManager()
login_manager.init_app(app)
# login_manager.login_view = 'login'
# login_manager.login_message = 'Please login!'

from Package import routes
