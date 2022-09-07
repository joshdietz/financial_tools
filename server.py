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
    return jsonify({'message': 'Hello, World!'})

@app.route('/login', methods=['POST'])
def login():
    # get the username and password from the request
    email = request.form['email']
    password = request.form['password']

    # connect to the database
    db = connect_db()

    # get the user from the database
    user = db.execute('SELECT * FROM users WHERE email = ?', (email,)).fetchone()

    # if the user exists and the password is correct, log them in
    if user is not None and check_password(password, user['password']):
        # set the user_id in the session
        session['user_id'] = user['id']
        # redirect to the dashboard
        return redirect(url_for('dashboard'))
    else:
        # redirect to the login page
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
    log('DB Setup: Starting...')
    if os.getenv('DB_DRIVER') == 'sqlite':
        if not os.path.exists(os.getenv('DB_NAME')):
            log('DB Setup: No database found. Creating new SQLite db in root project directory..')
            db = sqlite3.connect(os.getenv('DB_NAME'))
            # execute the schema.sql
            with open('schema.sql') as f:
                db.executescript(f.read())
            db.commit()
            db.close()
        else:
            log('DB Setup: SQLite database found. Skipping...')

if __name__ == '__main__':
    setup_database()
    app.run(debug=True)