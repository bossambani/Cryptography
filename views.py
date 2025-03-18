from flask import Flask, redirect, render_template, request,url_for, flash, Blueprint, jsonify
from werkzeug.security import generate_password_hash, check_password_hash
from model import db, User
views = Blueprint('views', __name__)

@views.route('/')
def home():
    return render_template("home.html")

@views.route('/signup') 
def signup_page():
    return render_template('signup.html')

@views.route('/api/signup', methods=['POST'])
def signup():
    data = request.get_json()

    username = data.get('username', '').strip()
    email = data.get('email', '').strip()
    password = data.get('password', '').strip()

    # Basic validation
    if not username or not email or not password:
        return jsonify({'error': 'All fields are required.'}), 400

    if User.query.filter_by(username=username).first():
        return jsonify({'error': 'Username already exists.'}), 409

    if User.query.filter_by(email=email).first():
        return jsonify({'error': 'Email already registered.'}), 409

    hashed_password = generate_password_hash(password)

    new_user = User(username=username, email=email, password=hashed_password)
    db.session.add(new_user)
    db.session.commit()

    return jsonify({'message': 'Signup successful'}), 201

@views.route("/login")
def login_page():
    return render_template("login.html")

@views.route("/api/login", methods=['POST'])
def login():
    data = request.get_json()

    username = data.get('username', '').strip()
    password = data.get('password', '').strip()

    if not username or not password:
        return jsonify({'error': 'All fields are required'}), 400
    
    user = User.query.filter_by(username=username).first()

    if user and check_password_hash(user.password, password):
        return jsonify({'message': 'Login Successfully'}), 200
    elif user:
        return jsonify({'error': 'Incorrect Password'}), 401
    else:
        return jsonify({'error': 'User does not exist'}), 404
  

@views.route('/ciphers')
def ciphers():
    cipher_list = [
        {'name': 'Caesar Cipher', 'description': 'A substitution cipher where each letter is shifted a fixed number of places.'},
        {'name': 'Vigenère Cipher', 'description': 'A method of encrypting alphabetic text using a keyword.'},
        {'name': 'Atbash Cipher', 'description': 'A cipher where each letter is replaced with its opposite in the alphabet.'},
        
    ]
    return render_template('ciphers.html', ciphers=cipher_list)

    


