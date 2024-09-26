from fastapi import FastAPI
from models import Todo

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

todos = []

#get all todos
@app.get("/todos")
async def create_todos(todo: Todo):
    todos.append(Todo)
    return {"message": "Todo has been added"}



#get single todo
@app.get("/todos{todo_id}")
async def get_todos(todo_id: int):
    for todo in todos:
        if todo.id == todo_id: 
            return {"todo":todo}
    return {"message": "No todos found"}


#create a todo

@app.post("/todo")
async def create_todos(todo:Todo):
    todos.append()
    return {"message": "todo has been added"}

#delete a todo
@app.delete("/todos/{todo_id}")
async def delete_todo(todo_id: int):
    for todo in todos:
        if todo.id == todo_id:
            todos.remove(todo)
            return{"message": "Todo has been DELETED!"}

    return {"mesage": "No todos found!"}

    #update a todo

@app.put("/todos/{todo_id}")
async def update_todo(todo_id: int, todo_obj: Todo):
     for todo in todos:
        if todo.id == todo_id:
            todo.id = todo_id
            todo_item = todo_obj.item
            return{"todo":todo}

     return{"No todos found"}