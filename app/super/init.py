'''
init 存放蓝图
models 存放登陆表单
views 安排路由
'''

from flask import Blueprint

super = Blueprint("super", __name__, url_prefix='/super')

from . import views
