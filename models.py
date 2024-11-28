# models.py

from sqlalchemy import Column, String, Boolean, DateTime, func
from database import Base

class Role(Base):
    __tablename__ = "roles"
    
    role_id = Column(String, primary_key=True, index=True)
    role_name = Column(String, index=True)
    status = Column(Boolean, default=True)
    timestamp = Column(DateTime(timezone=True), server_default=func.now())


