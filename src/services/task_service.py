from db.models import Task, User
from db.session import Session

def create_task(username: str, task_description: str) -> str:
    session = Session()
    user = session.query(User).filter_by(username=username).first()
    if not user:
        return f"User {username} not found."

    task = Task(assigned_user_id=user.user_id, task_description=task_description)
    session.add(task)
    session.commit()
    return f"Task assigned to {username}: {task_description}"

def list_tasks(user_id: int) -> str:
    session = Session()
    tasks = session.query(Task).filter_by(assigned_user_id=user_id).all()
    if not tasks:
        return "No tasks found."
    return "\n".join([f"Task ID: {task.task_id}, Description: {task.task_description}, Status: {task.status}" for task in tasks])
