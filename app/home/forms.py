from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, SelectField, TextAreaField
from wtforms.validators import DataRequired, ValidationError


class LoginForm(FlaskForm):
    account = StringField(
        label="学号",
        validators=[DataRequired()],
        render_kw={
            "class": "form-control",
            "placeholder": "请输入学号！"
        }
    )
    pswd = PasswordField(
        label="密码",
        validators=[DataRequired()],
        render_kw={
            "class": "form-control",
            "placeholder": "请输入密码"
        }
    )
    submit = SubmitField(
        label="登录",
        render_kw={
            "class": "btn btn-primary"
        }
    )


class RegisterForm(FlaskForm):
    s_id = StringField(
        label="学号",
        validators=[DataRequired()],
        render_kw={
            "class": "form-control",
            "placeholder": "请输入学号！"
        }
    )
    name = StringField(
        label="姓名",
        validators=[DataRequired()],
        render_kw={
            "class": "form-control",
            "placeholder": "your name?"
        }
    )
    pswd = PasswordField(
        label="密码",
        validators=[DataRequired()],
        render_kw={
            "class": "form-control",
            "placeholder": "请输入密码"
        }
    )
    email = StringField(
        label="邮箱",
        validators=[DataRequired()],
        render_kw={
            "class": "form-control",
            "placeholder": "请输入邮箱！"
        }
    )
    phone = StringField(
        label="手机号码",
        validators=[DataRequired()],
        render_kw={
            "class": "form-control",
            "placeholder": "请输入手机号码！"
        }
    )

    # ---------------------------------------------------
    logo = StringField(label="头像")

    sex = StringField(
        label="性别",
        validators=[DataRequired()],
        render_kw={
            "class": "form-control",
            "placeholder": "请输入性别！"
        }
    )
    school = SelectField(label="学院",
                         choices=[('通信工程学院', '通信工程学院'),
                                  ('电子工程学院', '电子工程学院'),
                                  ('计算机科学与技术学院', '计算机科学与技术学院'),
                                  ('机电工程学院', '机电工程学院'),
                                  ('物理与光电工程学院', '物理与光电工程学院'),
                                  ('经济与管理学院', '经济与管理学院'),
                                  ('数学与统计学院', '数学与统计学院'),
                                  ('生命科学技术学院', '生命科学技术学院'),
                                  ('空间科学与技术学院', '空间科学与技术学院'),
                                  ('先进材料与纳米技术学院', '先进材料与纳米技术学院'),
                                  ('网络与信息安全学院', '网络与信息安全学院'),
                                  ('人工智能学院', '人工智能学院'),
                                  ('马克思主义学院', '马克思主义学院'),
                                  ('人文学院', '人文学院')])
    department = StringField(
        label="第一志愿部门",
        validators=[DataRequired()],
        render_kw={
            "class": "form-control",
            "placeholder": "请输入第一志愿部门！"
        }
    )
    department2 = StringField(
        label="第二志愿部门",
        render_kw={
            "class": "form-control",
            "placeholder": "请输入第二志愿部门！"
        }
    )

    intro = TextAreaField(
        label="自我介绍",
        validators=[DataRequired()],
        render_kw={
            "class": "form-control",
            "placeholder": "出众的自我介绍能让学长学姐们更好的认识你们哦！"
        }
    )
    # ---------------------------------------------------

    classnum = StringField(
        label="班级",
        validators=[DataRequired()],
        render_kw={
            "class": "form-control",
            "placeholder": "请输入班级！"
        }
    )
    submit = SubmitField("注册")


class TestForm(FlaskForm):
    field1 = StringField("随便写一下什么")
    field2 = StringField("随便写一下什么")
    field3 = SubmitField("Submit")
