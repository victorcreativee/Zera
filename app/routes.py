from flask import Blueprint, render_template, request, redirect, url_for, flash

main = Blueprint('main', __name__)

auth = Blueprint('auth', __name__)

@main.route('/')
def home_redirect():
    return render_template('home.html')

@main.route('/home')
def homepage():
    return render_template('home.html')

@main.route('/about')
def about():
    return render_template('about.html')


@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        # Temporary logic for success
        if email == "test@example.com" and password == "password":
            flash("Login successful!", "success")
            return redirect(url_for('auth.login'))
        else:
            flash("Invalid credentials. Please try again.", "error")

    return render_template('login.html')

@auth.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form.get('username')
        email = request.form.get('email')
        password = request.form.get('password')

        if username and email and password:
            flash("Registration successful!", "success")
            return redirect(url_for('auth.register'))
        else:
            flash("Please fill in all fields.", "error")

    return render_template('register.html')