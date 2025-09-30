from typing import Iterable
from .models import Task

def tasks_to_dicts(tasks: Iterable[Task]):
    return [
        {
            "title": t.title,
            "duration": t.duration,
            "priority": t.priority,
            "sequence": t.sequence,
            "start": t.start.isoformat() if t.start else None,
            "assigned_start": t.assigned_start.isoformat() if t.assigned_start else None,
        }
        for t in tasks
    ]
