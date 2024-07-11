from pydantic import BaseModel


class Item(BaseModel):
    item: str
    status: str
