from app.extensions import database as db

class TodoList(db.Model):
    __tablename__ = "todo_lists"
    id = db.Column(db.Integer, primary_key=True, Index=True)
    title = db.Column(db.String(180), nullable=False)
    create_att = db.Column(db.DateTime)

    notes = db.relationship("Note", backref="todo_lists", lazy=True)
    user_owner_id = db.Column(db.Integer, db.ForeignKey("users.id"))

    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            if hasattr(self, key):
                setattr(self, key, value)
