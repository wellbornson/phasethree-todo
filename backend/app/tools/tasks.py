from typing import Optional, List
from sqlmodel import select, Session
from app.core.db import engine
from app.models.task import Task
from app.tools.mcp_server import mcp_server

@mcp_server.tool()
def add_task(user_id: str, title: str, description: Optional[str] = None) -> dict:
    """Quickly add a task."""
    try:
        with Session(engine) as session:
            task = Task(user_id=user_id, title=title, description=description)
            session.add(task)
            session.commit()
            return {"status": "success", "title": title}
    except:
        return {"status": "error"}

@mcp_server.tool()
def list_tasks(user_id: str, status: Optional[str] = "all") -> dict:
    """Quickly list tasks."""
    try:
        with Session(engine) as session:
            query = select(Task.id, Task.title, Task.completed).where(Task.user_id == user_id)
            if status == "pending":
                query = query.where(Task.completed == False)
            elif status == "completed":
                query = query.where(Task.completed == True)
            
            results = session.exec(query).all()
            return {
                "tasks": [{"id": r[0], "title": r[1], "completed": r[2]} for r in results]
            }
    except:
        return {"status": "error"}

@mcp_server.tool()
def complete_task(user_id: str, task_id: int) -> dict:
    """Quickly complete a task."""
    try:
        with Session(engine) as session:
            task = session.get(Task, task_id)
            if task and task.user_id == user_id:
                task.completed = True
                session.add(task)
                session.commit()
                return {"status": "success"}
            return {"status": "not_found"}
    except:
        return {"status": "error"}

@mcp_server.tool()
def delete_task(user_id: str, task_id: int) -> dict:
    """Delete a task."""
    try:
        with Session(engine) as session:
            task = session.get(Task, task_id)
            if task and task.user_id == user_id:
                session.delete(task)
                session.commit()
                return {"status": "success"}
            return {"status": "not_found"}
    except:
        return {"status": "error"}

@mcp_server.tool()
def update_task(user_id: str, task_id: int, title: Optional[str] = None, description: Optional[str] = None, completed: Optional[bool] = None) -> dict:
    """Update a task's details."""
    try:
        with Session(engine) as session:
            task = session.get(Task, task_id)
            if task and task.user_id == user_id:
                if title is not None: task.title = title
                if description is not None: task.description = description
                if completed is not None: task.completed = completed
                session.add(task)
                session.commit()
                return {"status": "success"}
            return {"status": "not_found"}
    except:
        return {"status": "error"}
