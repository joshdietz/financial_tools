import os
from toolbox import *
from flask import Flask, request, jsonify, render_template, redirect, url_for, session
from flask_bcrypt import Bcrypt
import sqlite3
import psycopg2
import dotenv

dotenv.load_dotenv()

app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('FLASK_SECRET_KEY')
bcrypt = Bcrypt(app)

@app.route('/', methods=['GET'])
def landing_page():
    # check if the user is logged in
    if 'user_id' in session:
        return redirect(url_for('dashboard'))
    else:
        return return_page('login.html', css='css/login.css', js='js/login.js')

@app.route('/dashboard', methods=['GET'])
def dashboard():
    # check if the user is logged in
    if 'user_id' in session:
        return jsonify({'message': 'You are logged in!'})
    else:
        return redirect(url_for('landing_page'))

@app.route('/login', methods=['POST'])
def login():
    # TODO: check number of failed login attempts for the user/IP, and block if necessary
    try:
        email = request.json['email']
        password = request.json['password']
    except KeyError as e:
        log('Login Error: ' + str(e), 'error')
        return jsonify({'response': 'Server Error: Invalid request'}), 400

    # connect to the database
    db = connect_db()

    # get the user from the database
    user = db.execute('SELECT * FROM users WHERE email = ?', (email,)).fetchone()

    # if the user exists and the password is correct, log them in
    if user is not None and check_password(password, user[2]):
        # set the user_id in the session
        session['user_id'] = user[0]

        response = jsonify({'response': 'success'})

    else:
        # see if a matching user exists
        if user is not None:
            # insert into login_attempts
            db.execute('INSERT INTO login_attempts (email, user_id, ip, status) VALUES (?, ?, ?, ?)', (email, user[0], request.remote_addr, "failed"))
        else:
            db.execute('INSERT INTO login_attempts (email, ip, status) VALUES (?, ?, ?)', (email, request.remote_addr, "failed"))
        
        db.commit()

        response = jsonify({'response': 'Invalid email or password'}), 401

    db.close()
    return response

@app.route('/register', methods=['GET'])
def register():
    return return_page('register.html', css='css/login.css', js='js/register.js')

@app.route('/register', methods=['POST'])
def register_user():
    try:
        email = request.json['email']
        password = request.json['password']
    except KeyError as e:
        log('Register Error: ' + str(e), 'error')
        return jsonify({'response': 'Server Error: Invalid request'}), 400

    # connect to the database
    db = connect_db()

    # check if the user already exists
    user = db.execute('SELECT * FROM users WHERE email = ?', (email,)).fetchone()

    if user is not None:
        # user already exists
        return jsonify({'response': 'User with that email already exists'}), 409

    # hash the password
    hashed_password = hash_password(password)

    # insert the user into the database
    db.execute('INSERT INTO users (email, password) VALUES (?, ?)', (email, hashed_password))
    db.commit()

    # get the user_id
    user_id = db.execute('SELECT id FROM users WHERE email = ?', (email,)).fetchone()[0]

    # set the user_id in the session
    session['user_id'] = user_id

    db.close()
    return jsonify({'response': 'success'})

@app.route('/logout', methods=['GET'])
def logout():
    # end the session
    session.clear()
    return redirect(url_for('landing_page'))

"""
    *** Helper Methods ***
"""
def hash_password(password):
    return bcrypt.generate_password_hash(password).decode('utf-8')

def check_password(password, hashed_password):
    return bcrypt.check_password_hash(hashed_password, password)

def return_page(page, css = None, js = None):
    # render the page into the main_template and return it
    if css is None:
        css = 'css/main.css'
    if js is None:
        js = 'js/main.js'
    return render_template('main_template.html', page=render_template(page), css=render_template(css), js=render_template(js))

def setup_database():
    log('Database: Running schema.sql...')
    if os.getenv('DB_DRIVER') == 'sqlite':
        db = sqlite3.connect(os.getenv('DB_NAME'))
        # execute the schema.sql
        with open('schema.sql') as f:
            try:
                db.executescript(f.read())
            except sqlite3.OperationalError as e:
                log('Database Error: ' + str(e), 'error')
                exit(1)
        db.commit()
        db.close()

if __name__ == '__main__':
    setup_database()
    app.run(debug=True)