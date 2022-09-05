import os
from flask import Flask, request, jsonify
from flask_bcrypt import Bcrypt
import dotenv

dotenv.load_dotenv()

app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('FLASK_SECRET_KEY')
bcrypt = Bcrypt(app)

@app.route('/', methods=['GET'])
def index():
    return jsonify({'page': 'index page'})

if __name__ == '__main__':
    app.run(debug=True)