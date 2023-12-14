from . import blueprint
from app.extensions import database
from app.forms import AddListForm
from app.models import TodoList

from datetime import datetime
from flask import redirect, url_for, request, flash, render_template
from flask_login import login_user, logout_user, login_required, current_user


@blueprint.route('/')
@login_required
def index():
    return render_template("index.html")

@blueprint.route('/my-lists', methods=["GET", "POST"])
@login_required
def my_lists():

    add_list_form = AddListForm()

    if request.method == "POST" and add_list_form.validate_on_submit():

        name = add_list_form.name.data
        icon = add_list_form.icon.data
        completed_att = add_list_form.date_completed.data

        new_list = TodoList(
            title=name,
            icon=icon,
            completed_att=completed_att,
            create_att=datetime.utcnow(),
            user_owner_id=current_user.id
        )
        
        database.session.add(new_list)
        database.session.commit()

        flash("List created with success", "success")
        return redirect(url_for("home.my_lists"))

    return render_template("mylists.html", form=add_list_form)

@blueprint.route('/my-lists/<list_id>', methods=["DELETE"])
@login_required
def my_lists_delete(list_id):
    list_id = int(list_id)
    todo_list = TodoList.query.filter(TodoList.user_owner_id == current_user.id, TodoList.id == list_id).first()
    if todo_list:
        database.session.delete(todo_list)
        database.session.commit()
        flash("list deleted with successfully", "success")
        return redirect(url_for("home.my_lists"))
    else:
        flash("list not found", "error")
        return redirect(url_for("home.my_lists"))

@blueprint.route('/my-tasks')
@login_required
def my_tasks():
    return render_template("mytasks.html")



