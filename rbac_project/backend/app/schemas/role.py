from pydantic import BaseModel

class RoleBase(BaseModel):
    name: str
    description: str | None = None

class RoleCreate(RoleBase):
    can_create: bool = False
    can_read: bool = False
    can_update: bool = False
    can_delete: bool = False
    can_share: bool = False
    can_manage_users: bool = False

class RoleResponse(RoleBase):
    id: int
    can_create: bool
    can_read: bool
    can_update: bool
    can_delete: bool
    can_share: bool
    can_manage_users: bool

    class Config:
        from_attributes = True