from Package import app, db # from __init__ import app db Object
import os

if __name__ == '__main__':
    # if system not found data.sqlite, then create an database
    if not os.path.exists('data.sqlite'):
        db.create_all()
    app.run(host='localhost',debug=True)
