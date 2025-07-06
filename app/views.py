from flask import Blueprint, request, jsonify, render_template, request
from . import db
from .models import Organization, Department , Resource, User, GuestLink
from flask_jwt_extended import jwt_required , get_jwt_identity
from .utils import has_role, generate_guest_token
from flask import session
from flask import redirect

views_bp = Blueprint("views", __name__)

@views_bp.route('/create_organization', methods=['POST'])
@jwt_required()
def create_organization():
    data = request.get_json()
    name = data.get("name")

    if Organization.query.filter_by(name=name).first():
        return jsonify({"error": "Organization already exists"}), 400

    org = Organization(name=name)
    db.session.add(org)
    db.session.commit()

    return jsonify({"message": "Organization created"}), 201


@views_bp.route('/create_department', methods=['POST'])
@jwt_required()
def create_department():
    data = request.get_json()
    name = data.get("name")
    org_id = data.get("organization_id")

    org = Organization.query.get(org_id)
    if not org:
        return jsonify({"error": "Organization not found"}), 404

    dept = Department(name=name, organization_id=org_id)
    db.session.add(dept)
    db.session.commit()

    return jsonify({"message": "Department created"}), 201

@views_bp.route('/secure_example', methods=['GET'])
@jwt_required()
def secure_example():
    current_user_id = get_jwt_identity()
    org_id = 1  # Example only

    if not has_role(current_user_id, ["Admin", "Manager"], org_id=org_id):
        return jsonify({"error": "Access denied"}), 403

    return jsonify({"message": "You have access!"})

@views_bp.route('/upload_resource', methods=['POST'])
@jwt_required()
def upload_resource():
    data = request.get_json()
    name = data.get("name")
    content = data.get("content")
    org_id = data.get("organization_id")
    dept_id = data.get("department_id")

    user_id = get_jwt_identity()

    # Only allow Admin, Manager, or Contributor to upload
    if not has_role(user_id, ["Admin", "Manager", "Contributor"], org_id=org_id, dept_id=dept_id):
        return jsonify({"error": "Permission denied"}), 403

    res = Resource(
        name=name,
        content=content,
        organization_id=org_id,
        department_id=dept_id,
        owner_id=user_id
    )

    db.session.add(res)
    db.session.commit()

    return jsonify({"message": "Resource uploaded"}), 201


@views_bp.route('/view_resource/<int:res_id>', methods=['GET'])
@jwt_required()
def view_resource(res_id):
    user_id = get_jwt_identity()
    res = Resource.query.get(res_id)

    if not res:
        return jsonify({"error": "Resource not found"}), 404

    # Only allow if user is Admin, Manager, Contributor, or Viewer
    if not has_role(user_id, ["Admin", "Manager", "Contributor", "Viewer"], org_id=res.organization_id, dept_id=res.department_id):
        return jsonify({"error": "Access denied"}), 403

    return jsonify({
        "id": res.id,
        "name": res.name,
        "content": res.content,
        "org": res.organization.name if res.organization else None,
        "dept": res.department.name if res.department else None
    })

@views_bp.route("/generate_guest_link", methods=["POST"])
@jwt_required()
def generate_guest_link():
    data = request.get_json()
    res_id = data.get("resource_id")
    permission = data.get("permission")  # "view" or "edit"

    if permission not in ["view", "edit"]:
        return jsonify({"error": "Invalid permission type"}), 400

    token = generate_guest_token()

    guest_link = GuestLink(
        token=token,
        resource_id=res_id,
        permission=permission
    )
    db.session.add(guest_link)
    db.session.commit()

    full_url = f"http://localhost:5000/guest_access/{token}"
    return jsonify({"guest_link": full_url}), 201


@views_bp.route("/guest_access/<string:token>", methods=["GET", "POST"])
def guest_access(token):
    guest_link = GuestLink.query.filter_by(token=token).first()

    if not guest_link:
        return jsonify({"error": "Invalid or expired guest token"}), 404

    resource = guest_link.resource

    if request.method == "GET":
        return jsonify({
            "resource_id": resource.id,
            "name": resource.name,
            "content": resource.content,
            "permission": guest_link.permission
        })

    elif request.method == "POST":
        if guest_link.permission != "edit":
            return jsonify({"error": "Edit not allowed"}), 403

        data = request.get_json()
        new_content = data.get("content")
        resource.content = new_content
        db.session.commit()

        return jsonify({"message": "Resource updated via guest link"})
    
@views_bp.route("/upload", methods=["GET"])
def upload_form():
    return render_template("upload.html", title="Upload Resource")


@views_bp.route("/upload_resource_form", methods=["POST"])
def upload_resource_form():
    from flask_jwt_extended import create_access_token
    # NOTE: In production you'd pass token securely
    name = request.form.get("name")
    content = request.form.get("content")
    org_id = int(request.form.get("organization_id"))
    dept_id = int(request.form.get("department_id"))

    # For demo purpose: assigning user_id = 1
    from .models import Resource
    resource = Resource(
        name=name,
        content=content,
        organization_id=org_id,
        department_id=dept_id,
        owner_id=1  # hardcoded for now
    )
    db.session.add(resource)
    db.session.commit()
    return "Resource uploaded"   

@views_bp.route("/", methods=["GET"])
def home():
    return "<h2>RBAC System Running ✅</h2><p><a href='/signup'>Go to Signup</a></p><p><a href='/login'>Go to Login</a></p>"


@views_bp.route('/init_roles_form', methods=["GET", "POST"])
def init_roles_form():
    from app.models import Role
    if request.method == "POST":
        default_roles = ["Admin", "Manager", "Contributor", "Viewer"]
        for role in default_roles:
            if not Role.query.filter_by(name=role).first():
                db.session.add(Role(name=role))
        db.session.commit()
        return "Roles initialized!"
    return render_template("init_roles.html", title="Init Roles")

@views_bp.route("/dashboard", methods=["GET", "POST"])
def dashboard():
    from app.models import Organization, Department, Role, Resource, GuestLink, UserRole

    message = ""
    user_id = session.get("user_id")
    if not user_id:
        return redirect("/login")  # For now, assume you're user ID 1

    if request.method == "POST":
        action = request.form.get("action")

        if action == "create_org":
            org_name = request.form.get("org_name")
            org = Organization(name=org_name)
            db.session.add(org)
            db.session.commit()
            message = f"Organization '{org_name}' created."

        elif action == "create_dept":
            dept_name = request.form.get("dept_name")
            org_id = request.form.get("dept_org_id")
            dept = Department(name=dept_name, organization_id=int(org_id))
            db.session.add(dept)
            db.session.commit()
            message = f"Department '{dept_name}' created under org ID {org_id}."

        elif action == "assign_role":
            role_name = request.form.get("role_name")
            org_id = request.form.get("role_org_id")
            dept_id = request.form.get("role_dept_id") or None

            from app.models import Role, UserRole

            role = Role.query.filter_by(name=role_name).first()
            if not role:
                message = f"Role {role_name} does not exist."
            else:
                user_role = UserRole(
                    user_id=user_id,
                    role_id=role.id,
                    organization_id=int(org_id) if org_id else None,
                    department_id=int(dept_id) if dept_id else None
                )
                db.session.add(user_role)
                db.session.commit()
                message = f"Assigned role '{role_name}' to you."

        elif action == "upload_resource":
            name = request.form.get("res_name")
            content = request.form.get("res_content")
            org_id = int(request.form.get("res_org_id"))
            dept_id = int(request.form.get("res_dept_id"))

            resource = Resource(
                name=name,
                content=content,
                organization_id=org_id,
                department_id=dept_id,
                owner_id=user_id
            )
            db.session.add(resource)
            db.session.commit()
            message = f"Resource '{name}' uploaded."

        elif action == "generate_guest":
            from app.utils import generate_guest_token

            res_id = int(request.form.get("guest_res_id"))
            permission = request.form.get("guest_permission")

            token = generate_guest_token()
            guest_link = GuestLink(
                token=token,
                resource_id=res_id,
                permission=permission
            )
            db.session.add(guest_link)
            db.session.commit()
            message = f"Guest link: http://localhost:5000/guest_access/{token}"

    orgs = Organization.query.all()
    depts = Department.query.all()
    roles = ["Admin", "Manager", "Contributor", "Viewer"]
    resources = Resource.query.all()

    return render_template("dashboard.html", title="Dashboard", message=message,
                           orgs=orgs, depts=depts, roles=roles, resources=resources)
