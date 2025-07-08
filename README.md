#  Flask Role-Based Access Control (RBAC) System

[![Python Version](https://img.shields.io/badge/Python-3.8%2B-blue.svg)](https://www.python.org/)
[![Flask Version](https://img.shields.io/badge/Flask-2.x-lightgrey.svg)](https://flask.palletsprojects.com/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![GitHub Stars](https://img.shields.io/github/stars/yourname/rbac_system?style=social)](https://github.com/yourname/rbac_system)

This project presents a **simple yet robust, production-style Role-Based Access Control (RBAC) system** built from the ground up using the Flask web framework. It demonstrates how to implement granular access control, ensuring that users can only interact with resources and functionalities aligned with their assigned roles and departmental affiliations.

---

##  Core Features & Capabilities

This system provides a comprehensive set of features for managing users, organizations, departments, and resources with fine-grained permissions:

| Feature                     | Description                                                                                                                                                                                               |
| :-------------------------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|  **JWT-based Authentication** | Secure user registration and login are managed using JSON Web Tokens (JWTs) for stateless and scalable authentication. Both session-based and JWT approaches can be implemented.                                  |
|  **Organizations & Departments** | Create and manage hierarchical structures with support for organizations and nested departments. This allows for clear segregation of data and user access based on organizational units.                     |
|  **Granular User Roles** | Defines a clear set of roles: `Admin`, `Manager`, `Contributor`, and `Viewer`. Each role comes with predefined permissions that dictate what a user can see, modify, or share within their assigned scope. |
|  **Resource Management** | Facilitates the secure upload, storage, and management of various digital resources (e.g., files, documents). Access to these resources is strictly controlled by the user's role and departmental affiliation. |
|  **Guest Link Sharing** | Enables the generation of secure, time-limited guest links for specific resources. These links provide either 'View' or 'Edit' access, similar to popular cloud document sharing services like Google Docs, without requiring guest authentication. |
|  **Interactive Dashboard** | All core functionalities, including user management, organization/department creation, resource upload, and role assignment, are accessible through a user-friendly HTML dashboard powered by Flask forms. No need for external API tools like Postman for basic operations. |

---

##  Getting Started

Follow these steps to get your Flask RBAC system up and running on your local machine.

### Prerequisites

* Python 3.8+
* `pip` (Python package installer)

### Installation

1.  **Clone the Repository:**
    ```bash
    git clone [https://github.com/yourname/rbac_system.git](https://github.com/yourname/rbac_system.git)
    cd rbac_system
    ```
    *(Remember to replace `yourname/rbac_system.git` with your actual GitHub repository URL)*

2.  **Create a Virtual Environment:**
    It's highly recommended to use a virtual environment to manage dependencies and avoid conflicts with other Python projects.
    ```bash
    python -m venv venv
    ```

3.  **Activate the Virtual Environment:**
    * **On Windows:**
        ```bash
        venv\Scripts\activate
        ```
    * **On macOS/Linux:**
        ```bash
        source venv/bin/activate
        ```

4.  **Install Dependencies:**
    All required Python packages are listed in `requirements.txt`.
    ```bash
    pip install -r requirements.txt
    ```

5.  **Run the Application:**
    This will start the Flask development server.
    ```bash
    python run.py
    ```

6.  **Access the Application:**
    Open your web browser and navigate to the signup page to get started:
    ```
    [http://127.0.0.1:5000/signup](http://127.0.0.1:5000/signup)
    ```
    From there, you can register new users, log in, and explore the dashboard functionalities.

---

##  Tech Stack

The project leverages a modern and efficient set of technologies:

* **Flask:** A lightweight and powerful Python web framework, ideal for building APIs and web applications.
* **Flask-JWT-Extended:** Provides robust support for JSON Web Tokens (JWTs) in Flask applications, handling authentication and authorization.
* **SQLAlchemy:** An SQL toolkit and Object-Relational Mapper (ORM) that provides a high-level API for interacting with databases, in this case, SQLite.
* **SQLite:** A lightweight, file-based relational database, perfect for local development and demonstration purposes.
* **HTML + Bootstrap:** Used for building a clean, responsive, and intuitive user interface for the dashboard.

---

##  Project Structure

The codebase is organized logically to separate concerns and enhance maintainability:

rbac_system/
├── app/                        # Main application package
│   ├── init.py             # Initializes the Flask app and database
│   ├── models.py               # Defines database models (Users, Organizations, Departments, Resources, etc.)
│   ├── views.py                # Contains Flask routes and logic for core application features (dashboard, resource management)
│   ├── auth.py                 # Handles user authentication (signup, login, logout, JWT handling)
│   ├── roles.py                # Defines role-based permissions and access control logic
│   ├── utils.py                # Utility functions (e.g., for file handling, token generation)
│   ├── templates/              # HTML templates for the user interface
│   │   ├── layout.html         # Base template for consistent page structure
│   │   ├── signup.html         # User registration form
│   │   ├── login.html          # User login form
│   │   └── dashboard.html      # Main user dashboard
├── config.py                   # Configuration settings for the Flask app (e.g., secret keys, database paths)
├── run.py                      # Entry point for running the Flask application
└── requirements.txt            # Lists all Python dependencies

---

##  Role Permissions Explained

The system implements a clear hierarchy of roles, each with specific capabilities:

| Role        | Can Upload Resources | Can Share Resources (Guest Links) | Can View Others' Resources (within scope) | Description                                                                                |
| :---------- | :------------------- | :-------------------------------- | :---------------------------------------- | :----------------------------------------------------------------------------------------- |
| **Admin** |  Yes               |  Yes                            |  Yes                                    | Full control. Can manage all users, organizations, departments, and resources.             |
| **Manager** |  Yes               |  Yes                            |  Yes                                    | Can manage users and resources within their assigned organization or department, including sharing. |
| **Contributor** |  Yes           |  No                             |  Yes                                    | Can upload and manage their own resources and view others' resources within their scope, but cannot share. |
| **Viewer** |  No                |  No                             |  Yes                                    | Can only view resources within their assigned organization or department. Cannot upload or share. |

These permissions ensure that access is granted on a "least privilege" basis, enhancing security.

---

##  Guest Link Functionality

The guest link feature provides a powerful way to share resources without requiring external users to register or log in.

* **Generation:** Users with appropriate permissions (e.g., Admin, Manager) can generate unique, secure links for specific resources.
* **Access Levels:** Links can be generated with two distinct access levels:
    * **View-only access:** Guests can see the content of the resource but cannot make any modifications.
    * **Edit access:** Guests are granted temporary permission to modify the resource.
* **Stateless Access:** Guests do not need to log in to access resources via these links. The access token embedded in the URL handles authentication.
* **Dynamic URLs:** The URLs are dynamically generated and look similar to this:
    ```
    [http://127.0.0.1:5000/guest_access/](http://127.0.0.1:5000/guest_access/)<token>
    ```
    Where `<token>` is a unique, signed JWT containing the resource ID and access permissions.

---

##  Contributing

Contributions, issues, and feature requests are welcome! Feel free to check the [issues page](https://github.com/yourname/rbac_system/issues).

1.  Fork the repository.
2.  Create your feature branch (`git checkout -b feature/AmazingFeature`).
3.  Commit your changes (`git commit -m 'Add some AmazingFeature'`).
4.  Push to the branch (`git push origin feature/AmazingFeature`).
5.  Open a Pull Request.

---

##  License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

##  Acknowledgments

* The Flask community for an excellent web framework.
* The creators of Flask-JWT-Extended and SQLAlchemy for their invaluable libraries.
* Bootstrap for providing a sleek and responsive UI framework.
