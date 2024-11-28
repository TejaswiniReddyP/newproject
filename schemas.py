from pydantic import BaseModel
from datetime import datetime
from typing import Optional, Union

class RoleSchema(BaseModel):
    role_id: str 
    role_name: str
    status: bool
    timestamp: datetime

class RoleCreate(BaseModel):
    role_name: str

class RoleUpdate(BaseModel):
    role_name: Optional[str] = None
    status: Optional[bool] = None

class Role(BaseModel):
    role_id: str  
    role_name: str
    status: bool
    timestamp: datetime

    class Config:
        orm_mode = True
