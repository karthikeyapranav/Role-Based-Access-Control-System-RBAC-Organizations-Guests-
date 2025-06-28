from .user import router as user_router
from .role import router as role_router
from .organization import router as organization_router
from .resource import router as resource_router
from .share import router as share_router
from .auth import router as auth_router  # Add this line
from .department import router as department_router  # Add this line

__all__ = [
    "user_router", 
    "role_router", 
    "organization_router", 
    "resource_router", 
    "share_router",
    "auth_router",  # Add this line
    "department_router"  # Add this line
]