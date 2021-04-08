from werkzeug.security import generate_password_hash, check_password_hash
from app_config import crete_datebase, app
from flask_login import UserMixin

# MySql Database 
db = crete_datebase(app)
# db.create_all()

# City Database Tables
class City(db.Model):
    __tablename__ = "city"

    def __init__(self, name, desc, img):
        self.name = name
        self.desc = desc
        self.img = img

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(180), unique=True, nullable=False)
    desc = db.Column(db.Text())
    img = db.Column(db.String(300))
    
    def __repr__(self):
        return '<City %r>' % self.name

class User(db.Model, UserMixin):
    __tablename__ = "user"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    first = db.Column(db.String(80), nullable=False)
    last = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(300), nullable=False)
    
    def __init__(self, username, first, last, password, email):
        self.username = username
        self.first = first
        self.last = last
        self.email = email
        self.password = generate_password_hash(password, salt_length=10)

    
    def __repr__(self):
        return '<User %r>' % self.username

    def verify_password(self, pwd):
        return check_password_hash(self.password, pwd)
