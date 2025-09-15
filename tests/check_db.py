from src.db import SessionLocal
from src.models import Company, User, Call

db = SessionLocal()

print("\n=== Companies ===")
companies = db.query(Company).all()
for c in companies:
    print(f"ID: {c.id}, Name: {c.name}")

print("\n=== Users ===")
users = db.query(User).all()
for u in users:
    print(f"ID: {u.id}, Name: {u.name}, Email: {u.email}, Company ID: {u.company_id}")

print("\n=== Calls ===")
calls = db.query(Call).all()
for call in calls:
    print(
        f"ID: {call.id}, "
        f"Company ID: {call.company_id}, User ID: {call.user_id}, "
        f"Phone: {call.phone_number}, Direction: {call.direction}, "
        f"Start: {call.start_time}, End: {call.end_time}, Duration: {call.duration_seconds}s, "
        f"Reason: {call.reason}, Result: {call.result}, Summary: {call.summary}, "
        f"Transcript: {call.transcript}"
    )

db.close()