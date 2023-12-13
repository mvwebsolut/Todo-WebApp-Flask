from flask import Blueprint

blueprint = Blueprint("home", __name__, url_prefix='/')

from .routes import *