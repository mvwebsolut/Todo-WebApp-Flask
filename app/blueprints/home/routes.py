from . import blueprint
from app.extensions import database

from datetime import datetime
from flask import redirect, url_for, request, flash, render_template
from flask_login import login_user, logout_user, login_required, current_user


@blueprint.route('/')
def index():
    return render_template("index.html")

