from flask import render_template
from app_config import app, db
from modals import City

@app.route('/')
def index():
    return render_template("index.html")


if __name__ == '__main__':
    app.run(debug=True)