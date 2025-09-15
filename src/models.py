# This file serves as the structure for each call to be stored in postgres

from sqlalchemy import Column, Integer, String, Text, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from .db import Base

class Company(Base):
    __tablename__ = "companies"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)

    # Relationships
    users = relationship("User", back_populates="company")
    calls = relationship("Call", back_populates="company")

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    email = Column(String, unique=True, index=True)
    company_id = Column(Integer, ForeignKey("companies.id"))

    # Relationships
    company = relationship("Company", back_populates="users")
    calls = relationship("Call", back_populates="user")

class Call(Base):
    __tablename__ = "calls"

    id = Column(Integer, primary_key=True, index=True) # unique ID for each call
    company_id = Column(Integer, ForeignKey("companies.id"))  # company ID for the user for this call
    user_id = Column(Integer, ForeignKey("users.id"))   # user ID for the user for this call

    phone_number = Column(String, index=True) # phone number of the caller/recipient
    direction = Column(String) # indicates incoming/outgoing call 
    start_time = Column(DateTime) # start time of the call in EST
    end_time = Column(DateTime) # end time of the call in EST
    duration_seconds = Column(Integer) # number of seconds the call lasted
    reason = Column(Text) # the reason Ringo called the user, or the reason the user called us
    result = Column(Text) # brief summary of what the call accomplished --> this is NOT the summary
    '''
                            "User booked a showing for x property at x Datetime"
                            "User was inquiring about houses between $200k-600k in X area"
                            "User wanted a quote on their 3 bed 3 bath house"
    '''
    summary = Column(Text) # more official summary
    transcript = Column(Text) # one-block transcript of the entire call

    company = relationship("Company", back_populates="calls")
    user = relationship("User", back_populates="calls")