from fastapi import APIRouter, Path
from app.schemas import TodoItem, Todo


todo_router = APIRouter()

todo_list = []


@todo_router.post("/add")
async def add_todo(todo: Todo) -> dict:
    todo_list.append(todo)
    return dict(message="success")


@todo_router.get("/")
async def get_todos() -> dict:
    return dict(todos=todo_list)


@todo_router.get("/{todo_id}")
async def get_todo(
        todo_id: int = Path(..., title="todo 객체의 id값")
) -> dict:

    for todo in todo_list:
        if todo.id == todo_id:
            return dict(todo=todo)

    return dict(message="조회된 TODO가 없습니다.")


@todo_router.put("/update/{todo_id}")
async def set_todo_item(
        todo_item: TodoItem,
        todo_id: int = Path(..., title="todo 객체의 id값")
) -> dict:
    for todo in todo_list:
        if todo.id == todo_id:
            todo.item.item = todo_item.item
            return dict(message="update success")

    return dict(message="조회된 TODO가 없습니다.")


@todo_router.delete("/delete/{todo_id}")
async def del_todo(
        todo_id: int = Path(..., title="todo 객체의 id값")
) -> dict:
    for idx, todo in enumerate(todo_list):
        if todo.id == todo_id:
            todo_list.pop(idx)
            return dict(message="remove success")

    return dict(message="조회된 TODO가 없습니다.")


@todo_router.delete("/delete_all")
async def clear_todo() -> dict:
    todo_list.clear()
    return dict(message="TODO List를 초기화 하였습니다.")
