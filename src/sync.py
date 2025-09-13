# This file sends the data from the retell API to postgres

from .retell_client import fetch_calls
from .nlp_client import query_openai
from .db import Base, engine, SessionLocal
from .models import Call
from datetime import datetime
import json

Base.metadata.create_all(bind=engine)

def sync_calls():
    db = SessionLocal()
    calls = fetch_calls()

    for call in calls:
        # get reason, result, and summary from GPT API
        rr_output = query_openai("reason_result", call["transcript"])
        rr_json = json.loads(rr_output) 
        summary = query_openai("summary", call["transcript"])

        db_call = Call(
            phone_number=call["phone_number"],
            direction=call["direction"],
            start_time=datetime.fromisoformat(call["start_time"]),
            end_time=datetime.fromisoformat(call["end_time"]),
            duration_seconds=call["duration_seconds"],
            reason=rr_json.get("reason"),
            result=rr_json.get("result"),
            summary=json.loads(summary),
            transcript=call["transcript"]
        )

        db.add(db_call)

    db.commit()
    db.close()
    print("Synced calls with reason, result, and summary!")

if __name__ == "__main__":
    sync_calls()
    print("Synced calls!")

