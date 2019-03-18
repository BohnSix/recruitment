'''
登陆表单
username, password
'''

from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, ValidationError

from recruitment.app.models import Admin


class LoginForm(FlaskForm):
    account = StringField(
        label="学号",
        validators=[DataRequired("请输入学号！")],
        description="请输入学号！",
        render_kw={
            "class": "form-control",
            "placeholder": "请输入学号"
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

    def validate_account(self, field):
        account = field.data
        admin = Admin.query.filter_by(name=account).count()
        if admin == 0:
            raise ValidationError("账号不存在")
