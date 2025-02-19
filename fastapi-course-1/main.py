from fastapi import FastAPI, HTTPException
from typing import Optional, List
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


class TodoCreate(TodoBase):  # Inherit from TodoBase. No need to add id
    pass


class Todo(TodoBase):  # Return the id + the TodoBase (title, description, priority)
    id: int = Field(..., description="Unique identifier of the todo")


class TodoUpdate(BaseModel):  # Inherit from TodoBase
    title: Optional[str] = Field(
        None, min_length=3, max_length=512, description="Title of the todo"
    )
    description: Optional[str] = Field(None, description="Description of the todo")
    priority: Optional[Prority] = Field(None, description="Priority of the todo")


# TODO: Let's create a simple API that will return a list of todos
# GET, POST, PUT, DELETE

all_todos = [
    Todo(id=1, title="Sports", description="Go to the gym", priority=Prority.HIGH),
    Todo(id=2, title="Read", description="Read 10 pages", priority=Prority.MEDIUM),
    Todo(id=3, title="Shop", description="Go shopping", priority=Prority.LOW),
    Todo(id=4, title="Study", description="Study for exam", priority=Prority.HIGH),
    Todo(
        id=5, title="Meditate", description="Meditate 20 minutes", priority=Prority.LOW
    ),
]



# @api.get("/")
# def index():
#     return {"message": "Hello World!"}


@api.get("/todos/{id}", response_model=Todo)
def get_todo(id: int):
    for todo in all_todos:
        if todo.id == id:
            return todo

    raise HTTPException(status_code=404, detail="Todo not found")


@api.get("/todos", response_model=List[Todo])
def get_todos(quantity: Optional[int] = None):
    if quantity:
        return all_todos[:quantity]
    else:
        return all_todos


@api.post("/todos", response_model=Todo)
def create_todo(todo: TodoCreate):
    id = max(todo.id for todo in all_todos) + 1  # | get the max id and increment by 1
    new_todo = Todo( 
        id=id, 
        title=todo.title, 
        description=todo.description, 
        priority=todo.priority
        )
    all_todos.append(new_todo)
    return new_todo


@api.put("/todos/{id}", response_model=Todo)
def update_todo(id: int, updated_todo: TodoUpdate):
    for todo in all_todos:
        if todo.id == id:
            if updated_todo.title is not None:
                todo.title = updated_todo.title
            if updated_todo.description is not None:
                todo.description = updated_todo.description
            if updated_todo.priority is not None:
                todo.priority = updated_todo.priority
            return todo

    raise HTTPException(status_code=404, detail="Todo not found")


@api.delete("/todos/{id}", response_model=Todo)
def delete_todo(id: int):
    for index, todo in enumerate(all_todos):  # enumerate to get the index
        if todo.id == id:
            deleted_todo = all_todos.pop(index)
            return deleted_todo

    raise HTTPException(status_code=404, detail="Todo not found")
