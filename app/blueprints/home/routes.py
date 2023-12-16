from . import blueprint
from app.extensions import database
from app.forms import AddListForm, AddTaskForm
from app.models import TodoList, User, Note

from datetime import datetime
from flask import redirect, url_for, request, flash, render_template
from flask_login import login_user, logout_user, login_required, current_user
from sqlalchemy import desc


@blueprint.route('/')
@login_required
def index():
    todo_lists = current_user.lists
    notes_desc = []
    for todo_list in todo_lists:
        notas = (
            Note.query
            .filter_by(todo_list_id=todo_list.id)
            .order_by(Note.create_att.desc())
            .all()
        )
        notes_desc.extend(notas)
    return render_template("index.html", latest_tasks=notes_desc)

@blueprint.route('/my-lists', methods=["GET", "POST"])
@login_required
def my_lists():

    add_list_form = AddListForm()

    if request.method == "POST" and add_list_form.validate_on_submit():

        
        name = add_list_form.name.data
        icon = add_list_form.icon.data

        new_list = TodoList(
            title=name,
            icon=icon,
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


@blueprint.route('/my-list/<list_id>', methods=["GET", "POST"])
@login_required
def my_list(list_id):

    add_task_form = AddTaskForm()
    todo_list = TodoList.query.filter(
        TodoList.user_owner_id == current_user.id,
        TodoList.id == list_id
    ).first()

    if request.method == "POST" and add_task_form.validate_on_submit():
        name = add_task_form.name.data
        done_att = add_task_form.done_att.data

        new_note = Note(
            text=name,
            done_att=done_att,
            create_att=datetime.utcnow()
        )

        todo_list.notes.append(new_note)

        database.session.add(new_note)
        database.session.commit()

        flash("Task added with success", "success")

        return redirect(request.url, 302)

    
    return render_template("mylist.html", form=add_task_form, list_data=todo_list)


@blueprint.route('/my-list/<list_id>', methods=["DELETE"])
@login_required
def my_list_delete(list_id):

    note_id = request.json['note_id']

    note = Note.query.filter(
        Note.todo_list_id == list_id,
        Note.id == note_id
    ).first()

    if note: 
        
        database.session.delete(note)
        database.session.commit()

        flash("Note deleted with success", "success")

        return redirect(request.url, 302)
    
    flash("Note not found", "error")
    
    return redirect(request.url, 302)


@blueprint.route('/my-list/<list_id>', methods=["PUT"])
@login_required
def my_list_complete(list_id):

    note_id = request.json['note_id']

    note = Note.query.filter(
        Note.todo_list_id == list_id,
        Note.id == note_id
    ).first()

    if note: 

        if note.completed:
            note.completed = False
        else:
            note.completed = True
        
        database.session.commit()

        flash("Note modified with success", "success")

        return redirect(request.url, 302)
    
    flash("Note not found", "error")

    return redirect(request.url, 302)







