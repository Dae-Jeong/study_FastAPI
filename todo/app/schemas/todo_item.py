from typing import List
from pydantic import BaseModel


class TodoItem(BaseModel):
    item: str

    class Config:
        json_schema_extra = {
            "example": {
                "item": "..?"
            }
        }


class TodoItems(BaseModel):
    todos: List[TodoItem]

    class Config:
        json_schema_extra = {
            "example": {
                "todos": [
                    {
                        "item": "example1"
                    },
                    {
                        "item": "example2"
                    }
                ]
            }
        }

