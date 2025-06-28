from fastapi import HTTPException, status
from app.models import User

def check_permission(user: User, permission: str):
    """Check if user has the required permission"""
    if not getattr(user.role, permission, False):
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail=f"You don't have permission to {permission.replace('_', ' ')}"
        )