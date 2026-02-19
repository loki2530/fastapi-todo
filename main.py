from fastapi import FastAPI,Depends,HTTPException
from schemas import Todo as TodoSchema,TodoCreate
from sqlalchemy.orm import Session 
from database import sessionLocal,Base,engine
from models import Todo
Base.metadata.create_all(bind=engine)
app=FastAPI()
# Dependency for DB session
def get_db():
    db=sessionLocal()
    try:
        yield db
    finally:
        db.close()

#POST route-create Todo

@app.post("/todos",response_model=TodoSchema)
def create(todo:TodoCreate,db:Session=Depends(get_db)):
    db_todo=Todo(**todo.dict())
    db.add(db_todo)
    db.commit()
    db.refresh(db_todo)
    return db_todo

# GET-all Todos
@app.get("/todos",response_model=list[TodoSchema])
def read_todos(db:Session=Depends(get_db)):
    return db.query(Todo).all()


#GET-single todos
@app.get("/todos/{todo_id}",response_model=TodoSchema)
def read_todo(todo_id:int,db:Session=Depends(get_db)):
    todo=db.query(Todo).filter(Todo.id==todo_id).first()
    if not todo:
        raise HTTPException(status_code=404,detail="todo not found")
    return todo

#PUT-update todo
@app.put("/todos/{todo_id}",response_model=TodoSchema)
def update_todo(todo_id:int,updated:TodoCreate,db:Session=Depends(get_db)):
    todo=db.query(Todo).filter(Todo.id==todo_id).first()
    if not todo:
        raise HTTPException(status_code=404,detail="Todo not found")
    for key,value in updated.dict().items():
        setattr(todo,key,value)
    db.commit()
    db.refresh(todo)
    return todo

# DELETE- Delete Todo
@app.delete("/todos/{todo_id}")
def del_todo(todo_id:int,db:Session=Depends(get_db)):
    todo=db.query(Todo).filter(Todo.id==todo_id).first()
    if not todo:
        raise HTTPException(status_code=404,detail="todo not founddd")
    db.delete(todo)
    db.commit()
    return{"message":"Todo Deleted Successfully"}
    