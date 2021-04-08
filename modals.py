from app_config import db

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