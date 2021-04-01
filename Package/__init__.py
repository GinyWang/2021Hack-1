from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)


# get current directory
current_dir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
# configurate the database URI
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + \
    os.path.join(current_dir, 'data.sqlite')

db = SQLAlchemy(app)



from Package import routes