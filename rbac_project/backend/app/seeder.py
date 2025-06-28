from app.database import SessionLocal
from app.models import Role

def seed_initial_data():
    db = SessionLocal()
    
    # Seed default roles
    roles = [
        {
            "name": "admin",
            "description": "System administrator with full access",
            "can_create": True,
            "can_read": True,
            "can_update": True,
            "can_delete": True,
            "can_share": True,
            "can_manage_users": True
        },
        {
            "name": "manager",
            "description": "Department manager with limited admin rights",
            "can_create": True,
            "can_read": True,
            "can_update": True,
            "can_delete": False,
            "can_share": True,
            "can_manage_users": False
        },
        {
            "name": "contributor",
            "description": "Regular user who can create content",
            "can_create": True,
            "can_read": True,
            "can_update": True,
            "can_delete": False,
            "can_share": False,
            "can_manage_users": False
        },
        {
            "name": "viewer",
            "description": "Read-only user",
            "can_create": False,
            "can_read": True,
            "can_update": False,
            "can_delete": False,
            "can_share": False,
            "can_manage_users": False
        }
    ]
    
    for role_data in roles:
        role = db.query(Role).filter_by(name=role_data["name"]).first()
        if not role:
            db.add(Role(**role_data))
    
    db.commit()
    db.close()

if __name__ == "__main__":
    seed_initial_data()