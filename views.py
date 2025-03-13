from flask import Flask, redirect, render_template, request,url_for, flash, Blueprint
from werkzeug.security import generate_password_hash, check_password_hash
from model import db, User
views = Blueprint('views', __name__)

@views.route('/')
def home():
    return render_template("home.html")

@views.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password1']
        confirm_password = request.form['password2']

        #validate password match
        if password != confirm_password:
            flash("Password do not match", "error")
            return redirect(url_for('views.signup'))
        
        #check if user already exist
        existing_user = User.query.filter((User.username == username) | (User.email == email)).first()
        if existing_user:
            flash("User already exists", "error")
            return redirect(url_for('views.signup'))
        
        #hash the password and register the user
        hashed_password = generate_password_hash(password)
        New_user = User(username=username, email=email, password=hashed_password)
        db.session.add(New_user)
        db.session.commit()
        flash("Account created successfully", "success")
        return redirect(url_for('views.login'))
    return render_template('signup.html')

@views.route("/login", methods=['GET', 'POST'])
def login():
    if request.method == "POST":
        username = request.form['username']
        password = request.form['password1']

        user = User.query.filter_by(username=username).first()
        if user:
            if check_password_hash(user.password, password):
                flash("Logged in Successfully!", "success")
                return redirect(url_for('views.cipher'))
            else:
                flash("Incorrect Password", 'error')
        else:
            flash("user does not exist", "error")

    return render_template('login.html')

@views.route('/ciphers')
def ciphers():
    cipher_list = [
        {'name': 'Caesar Cipher', 'description': 'A substitution cipher where each letter is shifted a fixed number of places.'},
        {'name': 'Vigenère Cipher', 'description': 'A method of encrypting alphabetic text using a keyword.'},
        {'name': 'Atbash Cipher', 'description': 'A cipher where each letter is replaced with its opposite in the alphabet.'},
        
    ]
    return render_template('ciphers.html', ciphers=cipher_list)

    


