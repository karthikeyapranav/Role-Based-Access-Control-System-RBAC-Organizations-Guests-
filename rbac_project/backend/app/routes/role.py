from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.models import Role
from app.schemas import RoleCreate, RoleResponse

router = APIRouter()

@router.post("/", response_model=RoleResponse)
def create_role(role: RoleCreate, db: Session = Depends(get_db)):
    try:
        db_role = Role(
            name=role.name,
            description=role.description,
            # Default permissions
            can_create=False,
            can_read=True,
            can_update=False,
            can_delete=False,
            can_share=False,
            can_manage_users=False
        )
        db.add(db_role)
        db.commit()
        db.refresh(db_role)
        return db_role
    except Exception as e:
        db.rollback()
        raise HTTPException(
            status_code=500, 
            detail=f"Error creating role: {str(e)}"
        )

@router.get("/{role_id}", response_model=RoleResponse)
def get_role(role_id: int, db: Session = Depends(get_db)):
    db_role = db.query(Role).filter(Role.id == role_id).first()
    if not db_role:
        raise HTTPException(status_code=404, detail="Role not found")
    return db_role