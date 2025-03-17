# app/__init__.py
from flask import Flask
from .models import db, bcrypt
from .routes import main
from .auth import auth

def create_app():
    app = Flask(__name__)
    app.config.from_object('config.Config')

    db.init_app(app)
    bcrypt.init_app(app)

    with app.app_context():
        db.create_all()  # Creates database tables

    app.register_blueprint(main)
    app.register_blueprint(auth)

    return app
