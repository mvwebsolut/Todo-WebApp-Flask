from app.extensions import database as db

class Note(db.Model):
    __tablename__ = "notes"
    id = db.Column(db.Integer, primary_key=True, Index=True)
    text = db.Column(db.String(200), nullable=False)
    completed = db.Column(db.Boolean, default=False)
    create_att = db.Column(db.DateTime)
    
    todo_list_id = db.Column(db.Integer, db.ForeignKey("todo_lists.id"))

    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            if hasattr(self, key):
                setattr(self, key, value)
