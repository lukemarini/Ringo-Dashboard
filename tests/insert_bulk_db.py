from datetime import datetime, timedelta, timezone
from src.db import SessionLocal
from src.models import Company, User, Call

db = SessionLocal()

def create_call(company_id, user_id, phone, direction, minutes, reason, result, summary, transcript):
    now = datetime.now(timezone.utc)
    return Call(
        company_id=company_id,
        user_id=user_id,
        phone_number=phone,
        direction=direction,
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
calls += [create_call(company1.id, emp1_c1.id, "+1555000001", "incoming", 5,
            "Asked about property on Oak St", "Sent details", "Caller requested property details.", "Transcript...") for _ in range(2)]
calls += [create_call(company1.id, emp2_c1.id, "+1555000002", "outgoing", 7,
            "Followed up on showing", "Confirmed appointment", "Confirmed Saturday showing.", "Transcript...") for _ in range(3)]

# Company 2
company2 = Company(name="Beta Homes")
db.add(company2)
db.commit(); db.refresh(company2)

emp1_c2 = User(name="Carol Consultant", email="carol@beta.com", company_id=company2.id)
emp2_c2 = User(name="Dan Dealer", email="dan@beta.com", company_id=company2.id)
db.add_all([emp1_c2, emp2_c2])
db.commit(); db.refresh(emp1_c2); db.refresh(emp2_c2)

calls += [create_call(company2.id, emp1_c2.id, "+1555000011", "incoming", 6,
            "Interested in condos", "Shared 3 condo listings", "Caller got condo details.", "Transcript...") for _ in range(4)]
calls += [create_call(company2.id, emp2_c2.id, "+1555000012", "incoming", 4,
            "Inquired about mortgage", "Provided mortgage info", "Caller received mortgage guidance.", "Transcript...") for _ in range(1)]

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

calls += [create_call(company3.id, emp1_c3.id, "+1555000021", "incoming", 8,
            "Asked about open houses", "Provided list of open houses", "Caller got open house info.", "Transcript...") for _ in range(1)]
calls += [create_call(company3.id, emp2_c3.id, "+1555000022", "outgoing", 5,
            "Follow-up on listing", "Sent follow-up email", "Caller received follow-up email.", "Transcript...") for _ in range(1)]
calls += [create_call(company3.id, emp3_c3.id, "+1555000023", "incoming", 9,
            "Wanted market report", "Sent market analysis", "Caller received market report.", "Transcript...") for _ in range(3)]
calls += [create_call(company3.id, emp4_c3.id, "+1555000024", "incoming", 10,
            "Asked about rental options", "Shared rental listings", "Caller got rental options.", "Transcript...") for _ in range(6)]

# Insert all calls
db.add_all(calls)
db.commit()

print("✅ Inserted mock companies, users, and calls!")

db.close()