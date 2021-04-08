from flask import Flask
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy


def create_app():
    app = Flask(__name__)
    Bootstrap(app)
    return app

# Database
def crete_datebase(app):
    # TODO: create a remote database
    app.config["SQLALCHEMY_DATABASE_URI"] = "mysql://root:devraj@127.0.0.1:3306/travelogue"
    app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
    db = SQLAlchemy(app)
    return db

# Flask App
app = create_app()

# MySql Database 
db = crete_datebase(app)
# db.create_all()
