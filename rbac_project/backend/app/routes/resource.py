from fastapi import APIRouter, Depends, HTTPException, UploadFile, File
from sqlalchemy.orm import Session
from datetime import datetime, timedelta
import secrets
from app.models import Resource, ShareLink, User  # <-- Added User import
from app.database import get_db
from app.auth import get_current_user

router = APIRouter(prefix="/resources", tags=["Resources"])

@router.post("/upload")
async def upload_file(
    file: UploadFile = File(...),
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)  # <-- Now User is defined
):
    # Save file to disk (example)
    file_path = f"uploads/{file.filename}"
    with open(file_path, "wb") as buffer:
        buffer.write(await file.read())
    
    # Create resource record
    db_resource = Resource(
        name=file.filename,
        file_path=file_path,
        organization_id=current_user.organization_id
    )
    db.add(db_resource)
    db.commit()
    return {"message": "File uploaded successfully"}

@router.post("/{resource_id}/share")
async def create_share_link(
    resource_id: int,
    permission: str,  # "view" or "edit"
    days_valid: int = 7,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)  # <-- User is defined
):
    # Generate unique token
    token = secrets.token_urlsafe(32)
    
    # Create share link
    db_link = ShareLink(
        token=token,
        resource_id=resource_id,
        expires_at=datetime.utcnow() + timedelta(days=days_valid),
        permission=permission,
        created_by=current_user.id
    )
    db.add(db_link)
    db.commit()
    return {"share_url": f"http://yourdomain.com/share/{token}"}