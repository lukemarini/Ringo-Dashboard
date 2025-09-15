# This file serves as the connection between the FastAPI app and Postgres

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# For local dev, later change to your Postgres connection string
DATABASE_URL = "postgresql+psycopg://voice_user:voice_pass@localhost:5432/voice_agent"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()