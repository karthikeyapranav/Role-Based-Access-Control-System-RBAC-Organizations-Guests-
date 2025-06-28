from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.schemas import OrganizationCreate, OrganizationResponse
from app.models import Organization, User
from app.database import get_db
from app.dependencies import check_admin_access

# Prefix already includes "/organizations", no need to repeat in route decorators
router = APIRouter(prefix="/organizations", tags=["Organizations"])

@router.post("/", response_model=OrganizationResponse)
def create_organization(
    org: OrganizationCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(check_admin_access)
):
    db_org = Organization(name=org.name)
    db.add(db_org)
    db.commit()
    db.refresh(db_org)
    return db_org

@router.get("/{org_id}", response_model=OrganizationResponse)
def get_organization(org_id: int, db: Session = Depends(get_db)):
    db_org = db.query(Organization).filter(Organization.id == org_id).first()
    if not db_org:
        raise HTTPException(status_code=404, detail="Organization not found")
    return db_org
