from Package import db


# User Post Assocation Table
# https://docs.sqlalchemy.org/en/14/orm/basic_relationships.html#many-to-many
 
user_post_table = db.Table('user_post_table',
    db.Column('post_id', db.Integer, db.ForeignKey('posts.id')),
    db.Column('user_id', db.Integer, db.ForeignKey('users.id'))
)

# Model of User
class User(db.Model):

    # Object User's attribute #
    __tablename__ = 'users'  # means that the data will be in SQLite's 'user' table
    id = db.Column(db.Integer, primary_key=True)    # unique id for the Object User
    name = db.Column(db.String(100), unique=True, nullable=False)   # unique name for the Object User, not be blank
    password = db.Column(db.String(100),nullable=False) # non-unique password for the Object User
      
    # initialization
    def __init__(self, name, password):
        self.name = name    # create Object User with name intialized
        self.password = password    # create Object User with name intialized

    
# Model of Post
class Post(db.Model):

    # Object User's attribute #
    __tablename__ = 'posts'  # means that the data will be in SQLite's 'post' table
    id = db.Column(db.Integer, primary_key=True)    # unique id for the Object Post
    title = db.Column(db.String(100), nullable=False)   # non-unique title for the Object Post
    content = db.Column(db.Text, nullable=False)    # non-unique content for the Object Post

    # initialization
    def __init__(self,title,content):
        self.title = title  # create Object Post with title intialized
        self.content = content  # create Object Post with content intialized