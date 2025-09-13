# This file serves as the FastAPI gateway

from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from . import db, models, schemas, crud

models.Base.metadata.create_all(bind=db.engine)

app = FastAPI()

def get_db():
    database = db.SessionLocal()
    try:
        yield database
    finally:
        database.close()

@app.get("/")
def root():
    return {"message": "Voice Agent Backend running!"}

# limited to 100 calls for now
@app.get("/calls", response_model=list[schemas.Call])
def read_calls(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.get_calls(db, skip=skip, limit=limit)

@app.post("/calls", response_model=schemas.Call)
def create_call(call: schemas.CallCreate, db: Session = Depends(get_db)):
    return crud.create_call(db, call)