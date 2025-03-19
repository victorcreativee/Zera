from flask import Flask
from .routes import main
from .models import db, bcrypt
from .auth import auth

def create_app():
    app = Flask(__name__)
    app.secret_key = 'supersecretkey'  # Required for flash messages

    app.config.from_object('config.Config')

    db.init_app(app)
    bcrypt.init_app(app)

    with app.app_context():
        db.create_all()

    app.register_blueprint(main)
    app.register_blueprint(auth)

    return app
