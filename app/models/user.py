from flask_login import UserMixin
from werkzeug.security import generate_password_hash

from app.extensions import database as db
from app.extensions import login_manager

class User(db.Model, UserMixin):

    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(120), nullable=False)
    last_name = db.Column(db.String(120), nullable=False)
    email = db.Column(db.String(255), nullable=False, unique=True)
    password = db.Column(db.String(255), nullable=False)
    create_att = db.Column(db.DateTime)

    lists = db.relationship("TodoList", backref='user', lazy=True)

    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            if hasattr(self, key):
                if key == "password":
                    value = generate_password_hash(value)
                setattr(self, key, value)

@login_manager.user_loader
def load_user(id):
    return User.query.filter_by(id=id).first()
