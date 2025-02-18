from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel, Field
from enum import IntEnum

api = FastAPI()
# $ uvicorn main:api --port 8000 --reload

""" 
Un objeto Pydantic (como todo) no se indexa como un diccionario -> todo['title']. 
En su lugar, se accede a sus atributos con la notación de punto -> todo.title.
"""


class Prority(IntEnum):
    LOW = 3
    MEDIUM = 2
    HIGH = 1


class TodoBase(BaseModel):
    title: str = Field(
        ..., min_length=3, max_length=512, description="Title of the todo"
    )
    description: str = Field(..., description="Description of the todo")
    priority: Prority = Field(default=Prority.LOW, description="Priority of the todo")


class TodoCreate(TodoBase):  # Inherit from TodoBase
    pass


class Todo(TodoBase):
    id: int = Field(..., description="Id of the todo")


class TodoUpdate(BaseModel):  # Inherit from TodoBase
    title: Optional[str] = Field(
        None, min_length=3, max_length=512, description="Title of the todo"
    )
    description: Optional[str] = Field(None, description="Description of the todo")
    priority: Optional[Prority] = Field(None, description="Priority of the todo")


# TODO: Let's create a simple API that will return a list of todos
# GET, POST, PUT, DELETE

all_todos = [
    {"id": 1, "title": "Sports", "description": "Go to the gym"},
    {"id": 2, "title": "Read", "description": "Read 10 pages"},
    {"id": 3, "title": "Shop", "description": "Go shopping"},
    {"id": 4, "title": "Study", "description": "Study for exam"},
    {"id": 5, "title": "Meditate", "description": "Meditate 20 minutes"},
]


@api.get("/")
def index():
    return {"message": "Hello World!"}


@api.get("/todos/{id}")
def get_todo(id: int):
    for todo in all_todos:
        if todo["id"] == id:
            return {"result": todo}
    return {"message": "Todo not found"}


@api.get("/todos")
def get_todos(quantity: Optional[int] = None):
    if quantity:
        return all_todos[:quantity]
    else:
        return {"result": all_todos}


@api.post("/todos")
def create_todo(todo: Todo):
    # we should validate inputs with pydantic
    id = (
        max(todo["id"] for todo in all_todos) + 1
    )  # | get the max id and increment by 1
    new_todo = {"id": id, "title": todo.title, "description": todo.description}
    all_todos.append(new_todo)
    return {"message": "Todo created successfully", "todo": new_todo}


@api.put("/todos/{id}")
def update_todo(id: int, updated_todo: Todo):
    for todo in all_todos:
        if todo["id"] == id:
            todo["title"] = updated_todo.title
            todo["description"] = updated_todo.description
            return {"message": "Todo updated successfully", "todo": todo}
    return {"error": "Todo not found"}


@api.delete("/todos/{id}")
def delete_todo(id: int):
    for todo in all_todos:
        if todo["id"] == id:
            all_todos.remove(todo)
            return {"message": "Todo deleted successfully"}
    return {"error": "Todo not found"}
