from .models import UserRole, Role
import uuid

def has_role(user_id, required_roles, org_id=None, dept_id=None):
    roles = UserRole.query.filter_by(user_id=user_id)

    if org_id:
        roles = roles.filter_by(organization_id=org_id)
    if dept_id:
        roles = roles.filter_by(department_id=dept_id)

    user_roles = roles.all()
    role_names = [r.role.name for r in user_roles]

    return any(role in role_names for role in required_roles)

def generate_guest_token():
    return str(uuid.uuid4())