from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.models import User, Role, Organization
from app.schemas import FirstAdminCreate, UserResponse  # Updated import
from app.auth import get_password_hash

router = APIRouter()

@router.post("/first-admin", response_model=UserResponse, tags=["Setup"])
def create_first_admin(
    user: FirstAdminCreate,
    db: Session = Depends(get_db)
):
    # Check if any admin exists
    if db.query(User).join(Role).filter(Role.name == "admin").first():
        raise HTTPException(400, "Admin user already exists")
    
    # Create default organization if none exists
    org = db.query(Organization).first()
    if not org:
        org = Organization(name="Default Organization")
        db.add(org)
        db.commit()
        db.refresh(org)
    
    # Get admin role
    admin_role = db.query(Role).filter(Role.name == "admin").first()
    if not admin_role:
        raise HTTPException(400, "Admin role doesn't exist. Run /setup/initial-role first")
    
    # Create admin user
    hashed_password = get_password_hash(user.password)
    db_user = User(
        username=user.username,
        email=user.email,
        hashed_password=hashed_password,
        role_id=admin_role.id,
        organization_id=org.id
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user