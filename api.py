from fastapi import FastAPI
from todo import todo_router

app = FastAPI()

@app.get("/")
async def root():
    return { "message": "Hello again! Hello Ruslan Islamov!"}

app.include_router(todo_router)