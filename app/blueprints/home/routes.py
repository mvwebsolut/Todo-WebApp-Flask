from . import blueprint
from app.extensions import database

from datetime import datetime
from flask import redirect, url_for, request, flash, render_template
from flask_login import login_user, logout_user, login_required, current_user


@blueprint.route('/')
@login_required
def index():
    return render_template("index.html")

@blueprint.route('/my-lists')
@login_required
def my_lists():
    return render_template("mylists.html")

@blueprint.route('/my-tasks')
@login_required
def my_tasks():
    return render_template("mytasks.html")



