from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="Inventory API")


class Item(BaseModel):
    name: str
    price: float
    in_stock: bool = True


items = [
    {"id": 1, "name": "Notebook", "price": 4.5, "in_stock": True},
    {"id": 2, "name": "Pen", "price": 1.25, "in_stock": False},
]


@app.get("/health")
def health_check():
    return {"status": "ok"}


# TODO: complete the remaining FastAPI routes for:
# - GET /items
# - POST /items
# - GET /items/{item_id}
# - PUT /items/{item_id}
# - DELETE /items/{item_id}
