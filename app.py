from flask import render_template
from app_config import app, db
from modals import City

@app.route('/')
def index():
    new_city = City("Kolkata", "Best in the world", "rajgir image")
    db.session.add(new_city)
    db.session.commit()
    return render_template("index.html")


if __name__ == '__main__':
    app.run(debug=True)