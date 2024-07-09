from pydantic import BaseModel
from app.schemas.item import Item


class Todo(BaseModel):
    id: int
    item: Item
