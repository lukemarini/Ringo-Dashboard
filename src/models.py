# This file serves as the structure for each call to be stored in postgres

from sqlalchemy import Column, Integer, String, Text, DateTime
from .db import Base

class Call(Base):
    __tablename__ = "calls"

    id = Column(Integer, primary_key=True, index=True) # unique ID for each call
    phone_number = Column(String, index=True) # phone number of the caller/recipient
    direction = Column(String) # indicates incoming/outgoing call 
    start_time = Column(DateTime) # start time of the call in EST
    end_time = Column(DateTime) # end time of the call in EST
    duration_seconds = Column(Integer) # number of seconds the call lasted
    reason = Column(Text) # the reason Ringo called the user, or the reason the user called us
    result = Column(Text) # brief summary of what the call accomplished --> this is NOT the summary (or maybe later it will be, up in the air for now)
    '''
                            "User booked a showing for x property at x Datetime"
                            "User was inquiring about houses between $200k-600k in X area"
                            "User wanted a quote on their 3 bed 3 bath house"
    '''
    transcript = Column(Text) # one-block transcript of the entire call