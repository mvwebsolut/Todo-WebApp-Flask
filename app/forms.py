from flask_wtf import FlaskForm
from wtforms import EmailField, StringField, PasswordField, BooleanField, SubmitField, DateField, Field
from wtforms.validators import DataRequired, Email, EqualTo

class LoginForm(FlaskForm):
    email = EmailField("Email", validators=[DataRequired(), Email()])
    password = PasswordField("Password", validators=[DataRequired()])
    remember_login = BooleanField("Remember")
    login = SubmitField("Login")

class RegisterForm(FlaskForm):
    first_name = StringField("FirstName", validators=[DataRequired()])
    last_name = StringField("LastName", validators=[DataRequired()])
    email = EmailField("Email", validators=[DataRequired(), Email()])
    password = PasswordField("Password", validators=[DataRequired()])
    accept_terms = BooleanField("TOS", validators=[DataRequired()])
    register = SubmitField("Register")

class AddListForm(FlaskForm):
    name = StringField("Name", validators=[DataRequired()])
    icon = StringField("Icon", validators=[DataRequired()])
    add = SubmitField("Add List")

class AddTaskForm(FlaskForm):
    name = StringField("Name", validators=[DataRequired()])
    done_att = DateField("Name", validators=[DataRequired()])
    add = SubmitField("Add Task")


