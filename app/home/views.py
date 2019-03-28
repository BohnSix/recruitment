from functools import wraps

from flask import flash, redirect, url_for, session, render_template, request
from flask_login import current_user, login_user, logout_user, login_required
from werkzeug.urls import url_parse

from recruitment.app.home.init import home
from recruitment.app.home.forms import LoginForm, RegisterForm
from recruitment.app.init import db
from recruitment.app.models import User, UserInfo


@home.route("/")
def index():
    return render_template("home/index.html")


@home.route('/login/', methods=["GET", "POST"])
def login():
    if current_user.is_authenticated:
        return redirect(url_for("home.index"))
    form = LoginForm()
    if form.validate_on_submit():
        data = form.data
        account = User.query.filter_by(s_id=data["account"]).first()
        if account is None:
            flash("账号不存在")
            return redirect(url_for("home.login"))
        if not account.check_pswd(data["pswd"]):
            flash("密码错误")
            return redirect(url_for("home.login"))
        login_user(account, remember=data["remember_me"])
        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc != "":
            return redirect(url_for("home.index"))
        return redirect(next_page)
    return render_template("home/login.html", form=form)


@login_required
@home.route("/logout/")
def logout():
    logout_user()
    return redirect(url_for("home.index"))


@home.route("/register/", methods=["GET", "POST"])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        data = form.data
        account = User.query.filter_by(s_id=data["s_id"]).count()
        if account != 0:
            messages = "账号已存在，请勿重复注册"
            flash(messages)
            return redirect(url_for("home.index", messages=messages))
        user = User(
            s_id=data["s_id"],
            name=data["name"]
        )
        user.set_pswd(data["pswd"])
        userinfo = UserInfo(
            user_id=data["s_id"],
            name=data["name"],
            sex=data["sex"],
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
        messages = "注册成功"
        flash(messages)
        return redirect(url_for("home.login", messages=messages))
    return render_template("home/register.html", form=form)


@login_required
@home.route("/userinfo/")
def userInfo():
    user = UserInfo.query.filter_by(user_id=current_user.s_id).first()

    return render_template("home/userinfo.html", user=user)
