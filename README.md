# 🛡️ Flask Role-Based Access Control (RBAC) System

This is a **simple but production-style RBAC system** built using Flask. It supports:

- 🔐 JWT-based authentication (sign up, login)
- 🏢 Organizations and nested Departments
- 👥 User Roles: Admin, Manager, Contributor, Viewer
- 📂 Resource Management (upload and control access)
- 🔗 Guest Link Sharing (View/Edit like Google Docs)

---

## 📁 Features

| Feature               | Description                                            |
|------------------------|--------------------------------------------------------|
| ✅ Auth               | Signup/Login using JWT or session                       |
| ✅ Org/Dept Nesting  | Create organizations and sub-departments                |
| ✅ RBAC              | Assign roles to users at org or dept level              |
| ✅ Resource Upload   | Upload resources scoped to org/dept                     |
| ✅ Guest Access      | Generate view/edit links for guests                     |
| ✅ HTML Dashboard    | All actions via Flask forms (no Postman needed)         |

---

## 🚀 Setup

1. Clone the repo:
git clone https://github.com/yourname/rbac_system.git
cd rbac_system

Create a virtual environment:
python -m venv venv
venv\Scripts\activate
Install dependencies:

pip install -r requirements.txt
Run the app:

python run.py
Open in browser:

arduino
http://127.0.0.1:5000/signup
✨ Tech Stack
Flask

Flask-JWT-Extended

SQLite (via SQLAlchemy)

HTML + Bootstrap (for UI)

📂 Folder Structure
arduino
Copy
Edit
rbac_system/
├── app/
│   ├── __init__.py
│   ├── models.py
│   ├── views.py
│   ├── auth.py
│   ├── roles.py
│   ├── utils.py
│   ├── templates/
│   │   ├── layout.html
│   │   ├── signup.html
│   │   ├── login.html
│   │   └── dashboard.html
├── config.py
├── run.py
└── requirements.txt

🔒 Role Permissions
Role	Can Upload	Can Share	Can View Others
Admin	✅	✅	✅
Manager	✅	✅	✅
Contributor	✅	❌	✅
Viewer	❌	❌	✅

🔗 Guest Links
Generate links with:

View-only access

Edit access

Guests don’t need to log in

URLs look like:

arduino
Copy
Edit
http://127.0.0.1:5000/guest_access/<token>



