from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, ValidationError


class LoginForm(FlaskForm):
    account = StringField(
        label="账号",
        validators=[DataRequired("请输入账号！")],
        description="请输入账号！",
        render_kw={
            "class": "form-control",
            "placeholder": "请输入账号"
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
