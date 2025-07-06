import os

BASE_DIR = os.path.abspath(os.path.dirname(__file__))

class Config:
    SECRET_KEY = "your_secret_key"
    JWT_SECRET_KEY = "jwt_secret_key"
    SQLALCHEMY_DATABASE_URI = "sqlite:///" + os.path.join(BASE_DIR, "rbac.db")  # 👈 forces DB in root
    SQLALCHEMY_TRACK_MODIFICATIONS = False
