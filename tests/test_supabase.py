from datetime import datetime, timedelta
from src.db import SessionLocal
from src import models

db = SessionLocal()

mock_call = models.Call(
    company_id=1,
    user_id=1,
    phone_number="+1555000000",
    direction="incoming",
    start_time=datetime.now(),
    end_time=datetime.now() + timedelta(minutes=5),
    duration_seconds=300,
    reason="Testing Supabase insert",
    result="Inserted via FastAPI",
    summary="This is just a test insert",
    transcript="CALLER: Hello\nAI: Hi there!"
)

db.add(mock_call)
db.commit()
db.refresh(mock_call)

print("Inserted:", mock_call.id)