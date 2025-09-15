from datetime import datetime, timedelta, timezone
from src.db import SessionLocal
from src.models import Company, User, Call

db = SessionLocal()

# Create a company
company = Company(name="Acme Realty")
db.add(company)
db.commit()
db.refresh(company)

# Create a user
user = User(name="Alice Agent", email="alice@acme.com", company_id=company.id)
db.add(user)
db.commit()
db.refresh(user)

# Create a call tied to both
call = Call(
    company_id=company.id,
    user_id=user.id,
    phone_number="+15551234567",
    direction="incoming",
    start_time=datetime.now(),
    end_time=datetime.now() + timedelta(minutes=5),
    duration_seconds=300,
    reason="The caller wanted to schedule a showing for a property.",
    result="The agent scheduled a showing for Saturday at 2 PM.",
    summary="The caller requested a showing, and the agent booked it for Saturday at 2 PM.",
    transcript="CALLER: Hi...\nAI: Sure...\nCALLER: Perfect."
)

db.add(call)
db.commit()

print("Inserted mock call with id:", call.id)

db.close()


