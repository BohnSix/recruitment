from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_script import Manager

app = Flask(__name__)
app.config['SQLALCHEMY_DATA_URI'] = ''
app.config['DATABASE_TRACK_MODIFICATIONS'] = True
app.config['SECRET_KEY'] = "a hard to guess string"
db = SQLAlchemy(app)
