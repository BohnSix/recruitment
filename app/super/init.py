from flask import Blueprint

super = Blueprint("super", __name__, url_prefix='/super')

from . import views
