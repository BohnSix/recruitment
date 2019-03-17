from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_script import Manager

from recruitment.app.admin.init import admin
from recruitment.app.home.init import home

app = Flask(__name__)
app.config['SQLALCHEMY_DATA_URI'] = ''
app.config['DATABASE_TRACK_MODIFICATIONS'] = True
app.config['DEBUG'] = True
app.config['SECRET_KEY'] = "a hard to guess string"

app.register_blueprint(admin)
app.register_blueprint(home)

db = SQLAlchemy(app)

manager = Manager(app)
