import os
from flask import Flask, request, jsonify
from flask_bcrypt import Bcrypt
import sqlite3
import psycopg2
import dotenv

dotenv.load_dotenv()

app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('FLASK_SECRET_KEY')
bcrypt = Bcrypt(app)

@app.route('/', methods=['GET'])
def index():
    return jsonify({'page': 'index page'})

"""
    *** Helper Methods ***
"""
def hash_password(password):
    return bcrypt.generate_password_hash(password).decode('utf-8')

def check_password(password, hashed_password):
    return bcrypt.check_password_hash(hashed_password, password)

def connect_db():
    if os.getenv('DB_DRIVER') == 'sqlite':
        return sqlite3.connect(os.getenv('DB_NAME'))
    elif os.getenv('DB_DRIVER') == 'postgres':
        return psycopg2.connect(os.getenv('DB_NAME'))

if __name__ == '__main__':
    app.run(debug=True)