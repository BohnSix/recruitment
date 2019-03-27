from functools import wraps

from flask import render_template, flash, redirect, url_for, session

from recruitment.app.admin.init import admin
from recruitment.app.admin.forms import LoginForm, RegisterForm, InterviewForm
from recruitment.app.exts import db
from recruitment.app.models import Admin, User, UserInfo

department = {
    "wailian": "外联部",
    "mishu": "秘书部",
    "bangongshi": "办公室"
}


def change_password(user_id, pswd):
    user = User.query.filter_by(s_id=user_id).first() or None
    if user:
        user.set_pswd(pswd)
        flash("密码修改成功")
    else:
        flash("用户不存在")


def admin_login_req(f):
    @wraps(f)
    def decorate_function(*args, **kwargs):
        if "admin" not in session:
            flash("你还没有登陆呢！")
            return redirect(url_for("admin.admin_login"))
        return f(*args, **kwargs)

    return decorate_function


@admin.route('/')
def index():
    return render_template("admin/index.html")


@admin.route("/login/", methods=["GET", "POST"])
def admin_login():
    form = LoginForm()
    if form.validate_on_submit():
        data = form.data
        admin = Admin.query.filter_by(name=data["account"]).first() or None
        if admin:
            if data["pswd"] != admin.pswd:
                flash("密码错误!")
                return redirect(url_for("admin.admin_login"))
            session["admin"] = data["account"]
            return redirect(url_for("admin.index", admin=admin))
    return render_template("admin/login.html", form=form)


@admin_login_req
@admin.route('/logout/')
def logout():
    session.pop('admin', None)
    print(session)
    return redirect(url_for("admin.index"))


@admin_login_req
@admin.route('/add/', methods=["GET", "POST"])
def add_fresh():
    form = RegisterForm()
    if form.validate_on_submit():
        data = form.data
        account = User.query.filter_by(s_id=data["s_id"]).count()
        if account != 0:
            messages = "账号已存在，请勿重复注册"
            flash(messages)
            return redirect(url_for("admin.index", messages=messages))
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
        return redirect(url_for("admin.login", messages=messages))
    return render_template("admin/register.html", form=form)


@admin_login_req
@admin.route('/show/')
def show():
    dep = department[session["admin"]]
    users = UserInfo.query.filter_by(department=dep)
    return render_template("admin/show.html", users=users)


@admin_login_req
@admin.route('/userinfo/<int:user_id>', methods=["GET", "POST"])
def userinfo(user_id):
    form = InterviewForm()
    userinfo = UserInfo.query.filter_by(user_id=user_id).first() or None
    if not userinfo:
        flash("没有找到这个人哦")
        return redirect(url_for("admin.index"))
    print(session)
    return render_template("admin/userinfo.html", userinfo=userinfo, form=form)
