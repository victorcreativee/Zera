from flask import Blueprint

main = Blueprint('main', '__name__')

@main.route('/')
def home():
    return "Welcome to ZERA Platform!"

@main.route('/home')
def homepage():
    return render_template('home.html')
