from fastapi import Depends, HTTPException, status
from app.auth import oauth2_scheme, get_current_user
from app.models import User

async def get_current_active_user(
    current_user: User = Depends(get_current_user)
):
    if not current_user.is_active:
        raise HTTPException(status_code=400, detail="Inactive user")
    return current_user

async def check_admin_access(
    user: User = Depends(get_current_active_user)
):
    if user.role.name != "admin":
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Admin access required"
        )
    return user