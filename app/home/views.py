from functools import wraps

from flask import flash, redirect, url_for, session, render_template, request

from recruitment.app.home.init import home
from recruitment.app.home.forms import LoginForm, RegisterForm
from recruitment.app.models import Freshman


@home.user_login_req
def user_login_req(f):
    @wraps(f)
    def decorate_function(*args, **kwargs):
        if "account" not in session:
            return redirect(url_for("home.login", next=request.url))
        return f(*args, **kwargs)

    return decorate_function


@home.route("/")
def index():
    user = session["freshman"]
    return render_template("index.html", user=user)


@home.route('/login', methods=["GET", "POST"])
def login():
    form = LoginForm()
    error = ""
    if form.validate_on_submit():
        data = form.data
        account = Freshman.query.fliter_by(name=data["account"]).first() or None
        if not Freshman.query.fliter_by(name="account"):
            error = "账号不存在"
            return redirect(url_for("home.login"))
        if not account.check_pswd(data["pswd"]):
            error = "密码错误"
            return redirect(url_for("home.login"))
        session["freshman"] = data.account
        return redirect(url_for("index"), error=error)


@home.user_login_req
@home.route("logout")
def logout():
    session.pop("freshman", None)
    print(session)
    return redirect(url_for("home.index"))


@home.route("/register")
def register():
    form = RegisterForm()



def user():
    pass


def index():
    pass


def login_log():
    pass
