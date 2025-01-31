from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

app = FastAPI()

# Модель для елементів
class Item(BaseModel):
    id: int
    name: str
    description: str

# Фейкове сховище
items_db = []

# Отримати всі елементи
@app.get("/items", response_model=List[Item])
def get_items():
    return items_db

# Отримати елемент за ID
@app.get("/items/{item_id}", response_model=Item)
def get_item(item_id: int):
    for item in items_db:
        if item.id == item_id:
            return item
    raise HTTPException(status_code=404, detail="Item not found")

# Додати новий елемент
@app.post("/items", response_model=Item)
def create_item(item: Item):
    items_db.append(item)
    return item

# Оновити елемент
@app.patch("/items/{item_id}", response_model=Item)
def update_item(item_id: int, updated_item: Item):
    for i, item in enumerate(items_db):
        if item.id == item_id:
            items_db[i] = updated_item
            return updated_item
    raise HTTPException(status_code=404, detail="Item not found")

# Видалити елемент
@app.delete("/items/{item_id}")
def delete_item(item_id: int):
    global items_db
    items_db = [item for item in items_db if item.id != item_id]
    return {"message": "Item deleted"}
