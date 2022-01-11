from flask import Flask,render_template
import pymongo

app = Flask(__name__)

client = pymongo.MongoClient('localhost', 27017)
db = client['user_login_system']

from user import routes

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/dashboard/')
def dashboard():
    return render_template('dashboard.html')