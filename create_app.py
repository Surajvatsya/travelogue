from flask_bootstrap import Bootstrap
from flask import Flask

def create_app():
    app = Flask(__name__)
    Bootstrap(app)
    return app