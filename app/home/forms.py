'''
登陆表单
username, password
'''

from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, SelectField
from wtforms.validators import DataRequired, ValidationError

from recruitment.app.models import User


class LoginForm(FlaskForm):
    account = StringField(
        label="学号",
        validators=[DataRequired("请输入学号！")],
        description="请输入学号！",
        render_kw={
            "class": "form-control",
            "placeholder": "请输入学号！"
        }
    )
    pswd = PasswordField(
        label="密码",
        validators=[DataRequired("请输入密码！")],
        description="请输入密码",
        render_kw={
            "class": "form-control",
            "placeholder": "请输入密码"
        }
    )
    submit = SubmitField(
        label="登录",
        render_kw={
            "class": "btn btn-primary btn-block btn-flat"
        }
    )

    def account_exist(self, field):
        account = field.data
        freshman = User.query.filter_by(name=account).count()
        if freshman == 0:
            raise ValidationError("账号不存在")


class RegisterForm(FlaskForm):
    s_id = StringField(
        label="学号",
        validators=[DataRequired("请输入学号！")],
        description="请输入学号！",
        render_kw={
            "class": "form-control",
            "placeholder": "请输入学号！"
        }
    )

    logo = StringField()

    name = StringField(
        label="邮箱",
        validators=[DataRequired("请输入邮箱！")],
        description="请输入邮箱！",
        render_kw={
            "class": "form-control",
            "placeholder": "请输入邮箱！"
        }
    )
    pswd = PasswordField(
        label="密码",
        validators=[DataRequired("请输入密码！")],
        description="请输入密码",
        render_kw={
            "class": "form-control",
            "placeholder": "请输入密码"
        }
    )
    email = StringField(
        label="邮箱",
        validators=[DataRequired("请输入邮箱！")],
        description="请输入邮箱！",
        render_kw={
            "class": "form-control",
            "placeholder": "请输入邮箱！"
        }
    )
    phone = StringField(
        label="手机号码",
        validators=[DataRequired("请输入手机号码！")],
        description="请输入手机号码！",
        render_kw={
            "class": "form-control",
            "placeholder": "请输入手机号码！"
        }
    )
    submit = SubmitField(
        label="注册",
        render_kw={
            "class": "btn btn-primary btn-block btn-flat"
        }
    )

    def account_exist(self, field):
        account = field.data
        user = User.query.filter_by(name=account).count()
        if user != 0:
            raise ValidationError("账号已存在")


class EnrollForm(FlaskForm):
    department = SelectField(
        label="意向部门",
        validators=[DataRequired("请选择意向部门！")],
        description="请选择意向部门！",
        render_kw={
            "class": "form-control",
            "placeholder": "请输入手机号码！"
        },
    ),
    phone = StringField(
        label="手机号码",
        validators=[DataRequired("请输入手机号码！")],
        description="请输入手机号码！",
        render_kw={
            "class": "form-control",
            "placeholder": "请输入手机号码！"
        }
    )
