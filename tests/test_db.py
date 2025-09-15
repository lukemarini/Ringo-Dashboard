from src.db import engine
from src.models import Base

print("Trying to connect...")

# This will create tables in your Postgres DB if they don’t exist yet
Base.metadata.create_all(bind=engine)

print("Tables created successfully!")