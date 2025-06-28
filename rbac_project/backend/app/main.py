from fastapi import FastAPI
from app.database import engine, Base
from app.models import User, Role, Organization, Department, Resource, ShareLink
from app.database import SessionLocal

# Create tables first (without auth requirements)
Base.metadata.create_all(bind=engine)

app = FastAPI(
    swagger_ui_init_oauth={
        "clientId": "swagger-ui",
        "scopes": ["openid", "profile", "email"]
    }
)

# Temporary unauthenticated endpoints for setup
from fastapi import APIRouter
setup_router = APIRouter()

@setup_router.post("/setup/initial-role", tags=["Setup"])
async def create_initial_role():
    db = SessionLocal()
    role = Role(
        name="admin",
        description="Full access",
        can_create=True,
        can_read=True,
        can_update=True,
        can_delete=True,
        can_share=True,
        can_manage_users=True
    )
    db.add(role)
    db.commit()
    return {"message": "Initial role created"}

app.include_router(setup_router)

# Now include your regular routers
from app.routes import (
    user_router, role_router, organization_router, 
    resource_router, share_router, auth_router, department_router
)

app.include_router(auth_router, prefix="/auth", tags=["Authentication"])
app.include_router(user_router, prefix="/users", tags=["Users"])
app.include_router(role_router, prefix="/roles", tags=["Roles"])
app.include_router(organization_router, prefix="/organizations", tags=["Organizations"])
app.include_router(department_router, prefix="/departments", tags=["Departments"])
app.include_router(resource_router, prefix="/resources", tags=["Resources"])
app.include_router(share_router, prefix="/share", tags=["Sharing"])

@app.get("/")
def read_root():
    return {"message": "RBAC System is running!"}