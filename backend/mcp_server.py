from mcp.server import Server
import mcp.types as types
from sqlmodel import Session, select
from backend.database import engine
from backend.models import Task

mcp_server = Server("todo-mcp-server")

@mcp_server.list_tools()
async def list_tools() -> list[types.Tool]:
    return [
        types.Tool(
            name="add_task",
            description="Add a new task. Requires a title.",
            inputSchema={
                "type": "object",
                "properties": {
                    "title": {"type": "string"},
                    "description": {"type": "string"}
                },
                "required": ["title"]
            }
        ),
        types.Tool(
            name="list_tasks",
            description="List all tasks. Optionally filter by completion status.",
            inputSchema={
                "type": "object",
                "properties": {
                    "completed": {"type": "boolean"}
                }
            }
        ),
        types.Tool(
            name="complete_task",
            description="Mark a task as completed by ID.",
            inputSchema={
                "type": "object",
                "properties": {
                    "task_id": {"type": "integer"}
                },
                "required": ["task_id"]
            }
        ),
        types.Tool(
            name="delete_task",
            description="Delete a task by ID.",
            inputSchema={
                "type": "object",
                "properties": {
                    "task_id": {"type": "integer"}
                },
                "required": ["task_id"]
            }
        ),
        types.Tool(
            name="update_task",
            description="Update a task's title or description.",
            inputSchema={
                "type": "object",
                "properties": {
                    "task_id": {"type": "integer"},
                    "title": {"type": "string"},
                    "description": {"type": "string"}
                },
                "required": ["task_id"]
            }
        )
    ]

@mcp_server.call_tool()
async def call_tool(name: str, arguments: dict) -> list[types.TextContent | types.ImageContent | types.EmbeddedResource]:
    with Session(engine) as session:
        if name == "add_task":
            task = Task(title=arguments["title"], description=arguments.get("description"))
            session.add(task)
            session.commit()
            session.refresh(task)
            return [types.TextContent(type="text", text=f"Task added: {task.id} - {task.title}")]
        
        elif name == "list_tasks":
            completed = arguments.get("completed")
            stmt = select(Task)
            if completed is not None:
                stmt = stmt.where(Task.completed == completed)
            tasks = session.exec(stmt).all()
            if not tasks:
                return [types.TextContent(type="text", text="No tasks found.")]
            text = "\n".join([f"[{'x' if t.completed else ' '}] {t.id}: {t.title}" for t in tasks])
            return [types.TextContent(type="text", text=text)]

        elif name == "complete_task":
            task = session.get(Task, arguments["task_id"])
            if task:
                task.completed = True
                session.add(task)
                session.commit()
                return [types.TextContent(type="text", text=f"Task {task.id} marked as completed.")]
            return [types.TextContent(type="text", text="Task not found.")]

        elif name == "delete_task":
            task = session.get(Task, arguments["task_id"])
            if task:
                session.delete(task)
                session.commit()
                return [types.TextContent(type="text", text=f"Task {arguments['task_id']} deleted.")]
            return [types.TextContent(type="text", text="Task not found.")]

        elif name == "update_task":
            task = session.get(Task, arguments["task_id"])
            if task:
                if "title" in arguments:
                    task.title = arguments["title"]
                if "description" in arguments:
                    task.description = arguments["description"]
                session.add(task)
                session.commit()
                return [types.TextContent(type="text", text=f"Task {task.id} updated.")]
            return [types.TextContent(type="text", text="Task not found.")]
            
        raise ValueError(f"Unknown tool: {name}")
