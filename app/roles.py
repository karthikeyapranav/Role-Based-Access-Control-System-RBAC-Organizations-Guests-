from flask import Blueprint, request, jsonify
from . import db
from .models import Role, User, UserRole, Organization, Department
from flask_jwt_extended import jwt_required, get_jwt_identity

roles_bp = Blueprint("roles", __name__)

# One-time role creation
@roles_bp.route("/init_roles", methods=["POST"])
def init_roles():
    default_roles = ["Admin", "Manager", "Contributor", "Viewer"]
    for role in default_roles:
        if not Role.query.filter_by(name=role).first():
            db.session.add(Role(name=role))
    db.session.commit()
    return jsonify({"message": "Roles initialized"}), 201


@roles_bp.route("/assign_role", methods=["POST"])
@jwt_required()
def assign_role():
    data = request.get_json()
    user_id = data.get("user_id")
    role_name = data.get("role_name")
    org_id = data.get("organization_id")
    dept_id = data.get("department_id")

    user = User.query.get(user_id)
    if not user:
        return jsonify({"error": "User not found"}), 404

    role = Role.query.filter_by(name=role_name).first()
    if not role:
        return jsonify({"error": "Invalid role name"}), 400

    new_role = UserRole(
        user_id=user.id,
        role_id=role.id,
        organization_id=org_id,
        department_id=dept_id
    )

    db.session.add(new_role)
    db.session.commit()

    return jsonify({"message": "Role assigned successfully"}), 201
