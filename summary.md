
---

## 📑 `summary.md` (for a pitch deck, report, or college submission)

```markdown
# Summary: Role-Based Access Control System with Guest Sharing

## Objective

Design and implement a secure, multi-layered Role-Based Access Control (RBAC) system that supports nested entities and Google Docs-style guest links.

---

## Key Features

- 🔐 **Authentication**
  - User signup and login
  - Token/session-based access

- 🏢 **Entities**
  - Organizations
  - Departments under organizations
  - Users with roles (Admin, Manager, Contributor, Viewer)

- 📂 **Resource Management**
  - Upload and store resources
  - Resources are scoped to organizations/departments

- 🔗 **Guest Link Sharing**
  - Generate public links with view/edit permissions
  - No login required to access

- 🧠 **Permissions**
  - Role-based access at both organization and department level
  - Only allowed users can perform actions based on their assigned role

---

## User Flow

1. Sign up / Login as user
2. Create an organization and departments
3. Assign roles to users
4. Upload resources
5. Generate guest links
6. Guests view/edit without needing login

---

## Tech Used

- **Flask** for backend API and routing
- **Flask-JWT-Extended** for secure authentication
- **SQLite + SQLAlchemy** for database and models
- **HTML templates** for form-based user interface

---

## Result

A working RBAC system with all CRUD permissions, role granularity, and public guest access — packaged in a lightweight Flask application with simple UI.

