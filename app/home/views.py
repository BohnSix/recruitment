import time
from functools import wraps

from flask import flash, redirect, url_for, session, render_template, request

from recruitment.app.home.init import home
from recruitment.app.home.forms import LoginForm, RegisterForm
from recruitment.app.init import db
from recruitment.app.models import User, UserInfo


def user_login_req(f):
    @wraps(f)
    def decorate_function(*args, **kwargs):
        if "account" not in session:
            return redirect(url_for("home.login", next=request.url))
        return f(*args, **kwargs)

    return decorate_function


@home.route("/")
def index():
    return render_template("home/index.html")


@home.route('/login/', methods=["GET", "POST"])
def login():
    form = LoginForm()
    error = ""
    if form.validate_on_submit():
        data = form.data
        account = User.query.filter_by(s_id=data["account"]).first() or None
        if not account:
            error = "账号不存在"
            flash(error)
            return redirect(url_for("home.login", error=error))
        if not account.check_pswd(data["pswd"]):
            error = "密码错误"
            flash(error)
            return redirect(url_for("home.login", error=error))
        session["account"] = data.account
    return render_template("home/login.html", form=form, error=error)


@user_login_req
@home.route("/logout")
def logout():
    session.pop("account", None)
    print(session)
    return redirect(url_for("home.index"))


@home.route("/register/", methods=["GET", "POST"])
def register():
    form = RegisterForm()
    error = ""
    if form.validate_on_submit():
        data = form.data
        account = User.query.filter_by(s_id=data["s_id"]).count()
        if account != 0:
            error = "账号已存在，请勿重复注册"
            flash(error)
            return redirect(url_for("home.index", error=error))
        user = User(
            s_id=data["s_id"],
            name=data["name"],
            pswd=data["pswd"],
        )
        userinfo = UserInfo(
            user_id=data["s_id"],
            name=data["name"],
            sex=data["sex"],
            logo=data["logo"],
            email=data["email"],
            phone=data["phone"],
            school=data["school"],
            department=data["department"],
            department2=data["department2"],
            intro=data["intro"],
            classnum=data["classnum"]
        )
        db.session.add(user)
        db.session.add(userinfo)
        db.session.commit()
        flash("注册成功", "OK")
        return redirect(url_for("home.login"))
    return render_template("home/register.html", form=form)


@user_login_req
@home.route("/userInfo/")
def userInfo():
    user = User.query.fliter_by(s_id=session["account"]).first()
    return render_template("userInfo.html", user=user)


@home.errorhandler(404)
def page_not_found(error):
    return render_template("home/404.html"), 404
