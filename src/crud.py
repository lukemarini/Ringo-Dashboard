# This file handles postgres database operations (create, read, update, delete)

from sqlalchemy.orm import Session
from . import models, schemas

# limit of 100 for now
def get_calls(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Call).offset(skip).limit(limit).all()

def create_call(db: Session, call: schemas.CallCreate):
    db_call = models.Call(**call.model_dump())
    db.add(db_call)
    db.commit()
    db.refresh(db_call)
    return db_call