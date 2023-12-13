from . import blueprint
from app.extensions import database
from app.models import User
from app.forms import LoginForm, RegisterForm

from datetime import datetime
from werkzeug.security import check_password_hash
from flask import redirect, url_for, request, flash, render_template
from flask_login import login_user, logout_user, login_required, current_user


@blueprint.route('/')
def index():

    if current_user.is_authenticated:
        return redirect(url_for("home.index"))

    return redirect(url_for("auth.login"))

@blueprint.route('/login', methods=["POST", "GET"])
def login():

    login_form = LoginForm()

    if current_user.is_authenticated:
        return redirect(url_for("home.index"))
    
    if request.method == "POST" and login_form.validate_on_submit():
        email = login_form.email.data
        password = login_form.password.data
        remember = login_form.remember_login.data

        user = User.query.filter_by(email=email).first()
        if not user:
            flash("inválid credentials", "error")
            return redirect(url_for("auth.login"))
        
        if not check_password_hash(user.password, password):
            flash("inválid credentials", "error")
            return redirect(url_for("auth.login"))
        
        flash("login realizado com sucesso", "success")
        login_user(user, remember)
        return redirect(url_for("home.index"))
        
    return render_template("login.html", form=login_form)

    
@blueprint.route('/register', methods=["POST", "GET"])
def register():

    register_form = RegisterForm()

    if current_user.is_authenticated:
        return redirect(url_for("home.index"))
    
    if request.method == "POST" and register_form.validate_on_submit():
        first_name = register_form.first_name.data
        last_name = register_form.last_name.data
        username = register_form.username.data
        password = register_form.password.data
        email = register_form.email.data

        user = User.query.filter_by(email=email).first()
        if user:
            flash("email already registred", "error")
            return redirect(url_for("auth.register"))
        
        user = User.query.filter_by(username=username).first()
        if user:
            flash("username already registred", "error")
            return redirect(url_for("auth.register"))
        
        new_user = User(
            first_name=first_name,
            last_name=last_name,
            username=username,
            email=email,
            password=password,
            create_att=datetime.utcnow()
        )
        database.session.add(new_user)
        database.session.commit()

        flash("registro realizado com sucesso", "success")
        login_user(new_user, True)
        return redirect(url_for("home.index"))
    
    return render_template("register.html", form=register_form)


@blueprint.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for("auth.login"))