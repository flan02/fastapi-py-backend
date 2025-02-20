from fastapi import FastAPI, Form, UploadFile, File
from typing import Optional, List
from pydantic import BaseModel, Field, field_validator, EmailStr

# $ uvicorn main:app --reload --port 8000

# initialize the FastAPI app

app = FastAPI()


@app.get("/")
def read_root():
    return {"message": "Hello World"}


# | Creating and managing routes


@app.post("/items")
def create_item(name: str, price: float):
    return {"name": name, "price": price}


@app.put("/items/{item_id}")
def update_item(item_id: int, name: str, price: float):
    return {"item_id": item_id, "name": name, "price": price}


@app.delete("/items/{item_id}")
def delete_item(item_id: int):
    return {"message": f"Item{item_id} deleted successfully"}


# | Path parameters 

@app.get('/users/{user_id}')
def road_user(user_id: int):
    return {"user_id": user_id}

@app.get('/items/{item_name}')
def road_user_item(item_name: str):
    return {"item_name": item_name}


# | Query parameters

@app.get('/users')
def road_user_params(user_id: int, name: Optional[str] = None):
    return {"user_id": user_id, "name": name}

# | Combining path and query parameters

@app.get('/users/{user_id}/details')
def read_user_details(user_id: int, include_email: bool = False):
    if include_email:
        return {
            "user_id": user_id,
            "include email:": "email included"
        }
    else:
        return {
            "user_id": user_id,
            "include email:": "email not included"
        }

# | Request and Response body

class User(BaseModel):
    name: str
    age: int = Field(..., gt=0, le=120)

    @field_validator("name")
    def name_must_not_be_empy(cls, v):
        if not v:
            raise ValueError("Name must not be empty")
        return v

@app.post('/users')
async def create_user(user: User):
    response = {"name": user.name, "age": user.age}
    return response

@app.get('/players/{player_id}', response_model=User)
async def get_player(player_id: int):
    return {
        "name": "Adam", 
        "age": 25
        }


""" 
Pydantic is a Python library for data parsing and validation using Python type annotations.
"""

# Advanced Validation with Pydantic
# Regular Expressions
# Custom validators
class Player(BaseModel):
    name: str = Field(..., pattern=r'^[a-zA-Z0-9_.\- ]+$')
    email: EmailStr
    age: int = Field(..., gt=0, le=100)

    @field_validator("name")
    def name_must_not_be_empy(cls, v):
        if not v:
            raise ValueError("name must not be empty")
        return v

@app.post('/register')
async def register_user(player: Player):
    return player


# | Handling Form Data and File Uploads

@app.post('/login')
async def login(username: str = Form(...), password: str = Form(...)):
    return {"username": username, "message": "Login successful"}

# ? Uploaded File
@app.post('/uploadfile')
async def create_upload_file(file: UploadFile = File(...)):
    return {"filename": file.filename}

# ? save upload file
@app.post('/savefile')
async def save_upload_file(file: UploadFile = File(...)):
    with open(f'uploads/{file.filename}', 'wb') as f:
        f.write(file.file.read())

    return { "message": f"File '{file.filename}' saved successfully" }

# ? multiple files
@app.post('/uploadfiles')
async def upload_multiple_files(files: List[UploadFile] = File(...)):
    return {"filenames": [file.filename for file in files]}