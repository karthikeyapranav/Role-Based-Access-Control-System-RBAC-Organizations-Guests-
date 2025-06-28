from pydantic import BaseModel, EmailStr
from typing import Optional

class UserBase(BaseModel):
    username: str
    email: EmailStr

class FirstAdminCreate(BaseModel):
    username: str
    email: EmailStr
    password: str

class UserCreate(UserBase):
    password: str
    organization_id: Optional[int] = None
    role_id: Optional[int] = None

class UserResponse(UserBase):
    id: int
    organization_id: int
    role_id: int

    class Config:
        from_attributes = True