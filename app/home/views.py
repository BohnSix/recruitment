from functools import wraps

from flask import flash, redirect, url_for, session, render_template

from recruitment.app.home.init import home
from recruitment.app.home.forms import LoginForm, RegisterForm
from recruitment.app.init import db
from recruitment.app.models import User, UserInfo


def user_login_req(f):
    @wraps(f)
    def decorate_function(*args, **kwargs):
        if "account" not in session:
            flash("你还没有登陆呢！")
            return redirect(url_for("home.login"))
        return f(*args, **kwargs)

    return decorate_function


@home.route("/")
def index():
    return render_template("home/index.html")


@home.route('/login/', methods=["GET", "POST"])
def login():
    form = LoginForm()
    session["account"] = None
    if form.validate_on_submit():
        data = form.data
        account = User.query.filter_by(s_id=data["account"]).first()
        if not account:
            flash("账号不存在")
            return redirect(url_for("home.login"))
        if not account.check_pswd(data["pswd"]):
            flash("密码错误")
            return redirect(url_for("home.login"))
        session["account"] = data["account"]
        user = account
        flash("欢迎回来， %s" % account.name)
        return render_template("home/index.html", form=form, user=user)
    return render_template("home/login.html", form=form)


@user_login_req
@home.route("/logout/")
def logout():
    session.pop("account", None)
    print(session)
    return redirect(url_for("admin.index"))


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


@user_login_req
@home.route("/userinfo/")
def userInfo():
    user = UserInfo.query.filter_by(user_id=session["account"]).first()

    return render_template("home/userinfo.html", user=user)
