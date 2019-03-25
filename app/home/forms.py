from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, SelectField, TextField
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
    name = StringField(
        label="姓名",
        validators=[DataRequired("我想知道你的名字哎！")],
        description="Tell me your name！",
        render_kw={
            "class": "form-control",
            "placeholder": "your name?"
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

    # ---------------------------------------------------
    logo = StringField()

    sex = StringField(
        label="性别",
        validators=[DataRequired("请输入性别！")],
        description="请输入性别！",
        render_kw={
            "class": "form-control",
            "placeholder": "请输入性别！"
        }
    )
    school = SelectField("这是什么呀", choices=[('01', '通信工程学院'),
                                           ('02', '电子信息工程学院'),
                                           ('03', '计算机科学与技术学院'),
                                           ('04', '机电工程学院'),
                                           ('05', '五元'),
                                           ('06', '经济与管理学院'),
                                           ('07', '七元')])
    department = StringField(
        label="第一志愿",
        validators=[DataRequired("请输入第一志愿部门！")],
        description="请输入第一志愿！",
        render_kw={
            "class": "form-control",
            "placeholder": "请输入第一志愿部门！"
        }
    )
    department2 = StringField(
        label="第二志愿",
        description="请输入第二志愿！",
        render_kw={
            "class": "form-control",
            "placeholder": "请输入第二志愿部门！"
        }
    )

    intro = TextField(
        label="自我介绍",
        validators=[DataRequired("简单的自我介绍下吧！")],
        description="自我介绍！",
        render_kw={
            "class": "form-control",
            "placeholder": "出众的自我介绍能让学长学姐们更好的认识你们哦！"
        }
    )
    # ---------------------------------------------------

    classnum = StringField(
        label="班级",
        validators=[DataRequired("请输入班级！")],
        description="请输入班级！",
        render_kw={
            "class": "form-control",
            "placeholder": "请输入班级！"
        }
    )
    submit = SubmitField(
        label="注册",
        render_kw={
            "class": "btn btn-primary btn-block btn-flat"
        }
    )
