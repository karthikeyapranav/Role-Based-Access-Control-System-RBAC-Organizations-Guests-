# Role-Based-Access-Control-System-RBAC-Organizations-Guests-
Secure RBAC System: A FastAPI-based Role-Based Access Control system with JWT authentication, organizational hierarchy, and secure resource sharing capabilities.  Features: Multi-level permissions, department management, expirable share links, and Swagger UI docs - ready for production deployment.

# RBAC System with FastAPI

![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-316192?style=for-the-badge&logo=postgresql&logoColor=white)

A production-ready Role-Based Access Control system with organizations, departments, and secure resource sharing.

## 🚀 Features

- **Secure Authentication**: JWT token-based auth with password hashing
- **Granular Permissions**: Admin/Manager/Contributor/Viewer roles
- **Organization Hierarchy**: Multi-level department structure
- **Resource Sharing**: Expirable view/edit links (like Google Docs)
- **API Documentation**: Interactive Swagger UI with auth support

## 📦 Installation

1. Clone the repository:
```bash = git clone https://github.com/karthikeyapranav/Role-Based-Access-Control-System-RBAC-Organizations-Guests-.git
Set up environment variables:

bash
cp backend/.env.example backend/.env
Start the system:

bash
docker-compose up -d --build

🔑 Initial Setup
Create admin role:

bash
curl -X POST http://localhost:8000/setup/initial-role
Create first admin user:

bash
curl -X POST http://localhost:8000/users/first-admin \
  -H "Content-Type: application/json" \
  -d '{
    "username": "admin",
    "email": "admin@company.com",
    "password": "admin123"
  }'
Get access token:

bash
curl -X POST http://localhost:8000/auth/token \
  -d "username=admin&password=admin123"
(Copy the access_token from response)

Authorize in Swagger UI:

Visit http://localhost:8000/docs

Click "Authorize" button (top-right)

Paste: Bearer YOUR_ACCESS_TOKEN

Click Authorize → Close

🌐 API Endpoints
Endpoint	Method	Description
/auth/token	POST	Get JWT token
/organizations/	POST	Create organization (Admin)
/departments/	POST	Create department
/resources/upload	POST	Upload file
/resources/{id}/share	POST	Create shareable link
🛠️ Development
To reset the database:

bash
docker-compose down -v
docker-compose up -d
