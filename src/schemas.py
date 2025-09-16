# This file formats data going in and out of the FastAPI app

from pydantic import BaseModel
from datetime import datetime, date
from typing import Optional

class CallBase(BaseModel):
    phone_number: str
    direction: str
    date: date
    start_time: datetime
    end_time: datetime
    duration_seconds: int
    reason: Optional[str] = None
    result: Optional[str] = None
    summary: Optional[str] = None
    transcript: Optional[str] = None

class CallCreate(CallBase):
    pass

class Call(CallBase):
    id: int

    class Config:
        orm_mode = True