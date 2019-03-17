'''
init 存放蓝图
models 存放登陆表单
views 安排路由
'''

from flask import Blueprint

home = Blueprint("home", __name__)
