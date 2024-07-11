from fastapi import APIRouter, Path, HTTPException, status, Request, Depends
from fastapi.templating import Jinja2Templates as Jinja
from starlette.templating import _TemplateResponse

from app.schemas import TodoItems, TodoItem, Todo


todo_router = APIRouter()

todo_list = []

templates = Jinja(directory="./templates/")


# 별도의 status_code를 반환하고 싶은 경우, 데코레이터에 status_code 매개변수로 전달
@todo_router.post("/add", status_code=201)
async def add_todo(
        request: Request,
        todo: Todo = Depends(Todo.as_form)
) -> _TemplateResponse:
    todo.id = len(todo_list) + 1
    todo_list.append(todo)

    # return dict(message="success")
    return templates.TemplateResponse(
        "todo.html",
        {
            "request": request,
            "todos": todo_list
        }
    )


@todo_router.get("/", response_model=TodoItems)
async def get_todos(request: Request) -> _TemplateResponse:
    # return dict(todos=todo_list)
    return templates.TemplateResponse(
        "todo.html",
        {
            "request": request,
            "todos": todo_list
        }
    )


@todo_router.get("/{todo_id}")
async def get_todo(
        request: Request,
        todo_id: int = Path(..., title="todo 객체의 id값")
) -> _TemplateResponse:

    for todo in todo_list:
        if todo.id == todo_id:
            return templates.TemplateResponse(
                "todo.html",
                {
                    "request": request,
                    "todo": todo
                }
            )

    # return dict(message="조회된 TODO가 없습니다.")
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="조회된 TODO가 없습니다."
    )


@todo_router.put("/update/{todo_id}")
async def set_todo_item(
        todo_item: TodoItem,
        todo_id: int = Path(..., title="todo 객체의 id값")
) -> dict:
    for todo in todo_list:
        if todo.id == todo_id:
            todo.item.item = todo_item.item
            return dict(message="update success")

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="수정을 위해 조회된 TODO가 없습니다."
    )


@todo_router.delete("/delete/{todo_id}")
async def del_todo(
        todo_id: int = Path(..., title="todo 객체의 id값")
) -> dict:
    for idx, todo in enumerate(todo_list):
        if todo.id == todo_id:
            todo_list.pop(idx)
            return dict(message="remove success")

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="삭제를 위해 조회된 TODO가 없습니다."
    )


@todo_router.delete("/delete_all")
async def clear_todo() -> dict:
    todo_list.clear()
    return dict(message="TODO List를 초기화 하였습니다.")
