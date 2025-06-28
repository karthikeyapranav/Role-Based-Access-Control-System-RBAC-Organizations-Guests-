from pydantic import BaseModel

class DepartmentBase(BaseModel):
    name: str
    organization_id: int

class DepartmentCreate(DepartmentBase):
    pass

class DepartmentResponse(DepartmentBase):
    id: int

    class Config:
        from_attributes = True  # For Pydantic v2 (replaces orm_mode)