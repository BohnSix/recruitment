from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from flask_script import Manager

from recruitment.app.exts import db, login_manager

from recruitment.app.admin.init import admin
from recruitment.app.home.init import home


def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root:root@localhost:3306/app'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
    app.config['DEBUG'] = True
    app.config['SECRET_KEY'] = "a hard to guess string"
    app.register_blueprint(admin, url_prefix='/admin')
    app.register_blueprint(home)

    login_manager.init_app(app)
    login_manager.login_view = "home.login"
    login_manager.login_message = "你得先登陆哦"
    db.init_app(app)
    return app


app = create_app()
db.create_all(app=app)
app.app_context().push()

bootstrap = Bootstrap(app)
manager = Manager(app)


@app.errorhandler(404)
def page_not_found(error):
    return render_template("home/404.html"), 404
