from flask import Flask
from flask_bootstrap import Bootstrap
from flask_script import Manager
import pymysql

from recruitment.app.exts import db

from recruitment.app.admin.init import admin
from recruitment.app.home.init import home

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:root@localhost:3306/app'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['DEBUG'] = True
app.config['SECRET_KEY'] = "a hard to guess string"

db.init_app(app)
bootstrap = Bootstrap(app)

app.register_blueprint(admin)
app.register_blueprint(home)

manager = Manager(app)
