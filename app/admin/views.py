from flask import render_template, flash, redirect, url_for, session

from recruitment.app.admin.init import admin
from recruitment.app.admin.forms import LoginForm
from recruitment.app.models import Admin


def change_password():
    pass


def admin_login_req():
    pass


@admin.route('/')
# @admin_login_req
def index():
    return render_template("index.html")


@admin.route("login", methods=["GET", "POST"])
def admin_login():
    form = LoginForm()
    if form.validate_on_submit():
        data = form.data
        admin1 = Admin.query.fliter_by(name=data["account"]).first()
        if not admin1.check_pswd(data["pswd"]):
            flash("密码错误")
            return redirect(url_for("admin.admin_login"))
        session['admin'] = data['account']
        return redirect()

