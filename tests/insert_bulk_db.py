from datetime import datetime, timedelta, timezone
from src.db import SessionLocal
from src.models import Company, User, Call

db = SessionLocal()

def create_call(company_id, user_id, phone, direction, minutes, reason, result, summary, transcript, offset_days=0, offset_minutes=0):
    now = datetime.now(timezone.utc) + timedelta(days=offset_days, minutes=offset_minutes)
    return Call(
        company_id=company_id,
        user_id=user_id,
        phone_number=phone,
        direction=direction,
        date=now.date(), 
        start_time=now,
        end_time=now + timedelta(minutes=minutes),
        duration_seconds=minutes * 60,
        reason=reason,
        result=result,
        summary=summary,
        transcript=transcript
    )

# Company 1
company1 = Company(name="Acme Realty")
db.add(company1)
db.commit(); db.refresh(company1)

emp1_c1 = User(name="Alice Agent", email="alice@acme.com", company_id=company1.id)
emp2_c1 = User(name="Bob Broker", email="bob@acme.com", company_id=company1.id)
db.add_all([emp1_c1, emp2_c1])
db.commit(); db.refresh(emp1_c1); db.refresh(emp2_c1)

calls = []
for i in range(2):
    calls.append(create_call(company1.id, emp1_c1.id, "+1555000001", "incoming", 5,
        "Asked about property on Oak St", "Sent details",
        f"Caller requested property details. Call #{i+1}",
        "Transcript...", offset_days=i, offset_minutes=i*3))

for i in range(3):
    calls.append(create_call(company1.id, emp2_c1.id, "+1555000002", "outgoing", 7,
        "Followed up on showing", "Confirmed appointment",
        f"Confirmed Saturday showing. Call #{i+1}",
        "Transcript...", offset_days=i, offset_minutes=i*4))

# Company 2
company2 = Company(name="Beta Homes")
db.add(company2)
db.commit(); db.refresh(company2)

emp1_c2 = User(name="Carol Consultant", email="carol@beta.com", company_id=company2.id)
emp2_c2 = User(name="Dan Dealer", email="dan@beta.com", company_id=company2.id)
db.add_all([emp1_c2, emp2_c2])
db.commit(); db.refresh(emp1_c2); db.refresh(emp2_c2)

for i in range(4):
    calls.append(create_call(company2.id, emp1_c2.id, "+1555000011", "incoming", 6,
        "Interested in condos", "Shared 3 condo listings",
        f"Caller got condo details. Call #{i+1}",
        "Transcript...", offset_days=5+i, offset_minutes=i*5))

calls.append(create_call(company2.id, emp2_c2.id, "+1555000012", "incoming", 4,
    "Inquired about mortgage", "Provided mortgage info",
    "Caller received mortgage guidance. Call #1",
    "Transcript...", offset_days=10))

# Company 3
company3 = Company(name="Castle Realty")
db.add(company3)
db.commit(); db.refresh(company3)

emp1_c3 = User(name="Eve Expert", email="eve@castle.com", company_id=company3.id)
emp2_c3 = User(name="Frank Finder", email="frank@castle.com", company_id=company3.id)
emp3_c3 = User(name="Grace Guide", email="grace@castle.com", company_id=company3.id)
emp4_c3 = User(name="Hank Helper", email="hank@castle.com", company_id=company3.id)
db.add_all([emp1_c3, emp2_c3, emp3_c3, emp4_c3])
db.commit(); db.refresh(emp1_c3); db.refresh(emp2_c3); db.refresh(emp3_c3); db.refresh(emp4_c3)

calls.append(create_call(company3.id, emp1_c3.id, "+1555000021", "incoming", 8,
    "Asked about open houses", "Provided list of open houses",
    "Caller got open house info.", "Transcript...", offset_days=15))

calls.append(create_call(company3.id, emp2_c3.id, "+1555000022", "outgoing", 5,
    "Follow-up on listing", "Sent follow-up email",
    "Caller received follow-up email.", "Transcript...", offset_days=16))

for i in range(3):
    calls.append(create_call(company3.id, emp3_c3.id, "+1555000023", "incoming", 9,
        "Wanted market report", "Sent market analysis",
        f"Caller received market report. Call #{i+1}",
        "Transcript...", offset_days=17+i))

for i in range(6):
    calls.append(create_call(company3.id, emp4_c3.id, "+1555000024", "incoming", 10,
        "Asked about rental options", "Shared rental listings",
        f"Caller got rental options. Call #{i+1}",
        "Transcript...", offset_days=20+i))

# Insert all calls
db.add_all(calls)
db.commit()

print("✅ Inserted mock companies, users, and unique dated calls!")

db.close()
