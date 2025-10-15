from fastapi import APIRouter, Path, Query, HTTPException, status
from model import Todo, TodoItem, TodoItems

todo_router = APIRouter()

todo_list = []

@todo_router.post("/todo", status_code=201)
async def add_todo(todo: Todo) -> dict:
    todo_list.append(todo)
    return {"message": "Todo добавлен успешно!"}

@todo_router.get("/todo", response_model=TodoItems)
async def retrieve_todos() -> dict:
    return {"todos": todo_list}

@todo_router.get("/todo/{todo_id}")
async def get_single_todo(todo_id: int = Path(..., title="The ID of the todo to retrieve.")) -> dict:
    for todo in todo_list:
        if todo.id == todo_id:
            return {
                "todo": todo
            }
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Задача с указанным ID не найдена."
    )

@todo_router.get("/search/")
async def query_route(query: str = Query(None)):
    return {"query": query}

@todo_router.put("/todo/{todo_id}")
async def update_todo(todo_data: TodoItem, todo_id: int = Path(..., title="ID задачи")) -> dict:
    for todo in todo_list:
        if todo.id == todo_id:
            todo.item = todo_data.item
            return {
                "message": "Задача обновлена."
            }
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Задача с указанным ID не найдена."
    )

@todo_router.delete("/todo/{todo_id}")
async def delete_single_todo(todo_id: int) -> dict:
    for index in range(len(todo_list)):
        todo = todo_list[index]
        if todo.id == todo_id:
            todo_list.pop(index)
            return {"message": "Задача удалена."}
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Задача с указанным ID не найдена."
    )