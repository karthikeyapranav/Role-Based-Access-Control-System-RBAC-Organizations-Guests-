from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.models import ShareLink, Resource
from app.database import get_db
from datetime import datetime

router = APIRouter(prefix="/share", tags=["Sharing"])

@router.get("/{token}")
async def access_via_share(
    token: str,
    db: Session = Depends(get_db)
):
    # Check if share link is valid
    share_link = db.query(ShareLink).filter(
        ShareLink.token == token,
        ShareLink.expires_at > datetime.utcnow()
    ).first()
    
    if not share_link:
        raise HTTPException(404, detail="Invalid or expired link")
    
    # Get the resource
    resource = db.query(Resource).filter(Resource.id == share_link.resource_id).first()
    
    # Return based on permission
    if share_link.permission == "view":
        return {"resource": resource.name, "access": "view-only"}
    else:
        return {"resource": resource.name, "access": "edit-allowed"}