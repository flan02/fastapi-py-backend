from fastapi import FastAPI

# $ uvicorn main:app --reload --port 8000 main.py

# initialize the FastAPI app

app = FastAPI()


@app.get("/")
def read_root():
    return {"message": "Hello World"}


# Creating and managing routes


@app.post("/items")
def create_item(name: str, price: float):
    return {"name": name, "price": price}


@app.put("/items/{item_id}")
def update_item(item_id: int, name: str, price: float):
    return {"item_id": item_id, "name": name, "price": price}


@app.delete("/items/{item_id}")
def delete_item(item_id: int):
    return {"message": f"Item{item_id} deleted successfully"}


# Path parameters and Query parameters

@app.get('/users/{user_id}')
def road_user(user_id: int):
    return {"user_id": user_id}

@app.get('/items/{item_name}')
def road_user_item(item_name: str):
    return {"item_name": item_name}