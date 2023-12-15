from .extensions import database
from app.models import TodoList, Note

def completed_tasks_filter(list_id: int) -> int:
    list_data = TodoList.query.filter_by(id=list_id).first()
    completed_count = 0
    if list_data:
        for note in list_data.notes:
            if note.completed:
                completed_count += 1
    return completed_count

