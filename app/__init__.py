from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager

db = SQLAlchemy()
jwt = JWTManager()

def create_app():
    app = Flask(__name__)
    app.config.from_object("config.Config")

    db.init_app(app)
    jwt.init_app(app)

    from .auth import auth_bp
    from .views import views_bp
    from .roles import roles_bp

    app.register_blueprint(auth_bp)
    app.register_blueprint(views_bp)
    app.register_blueprint(roles_bp)

    with app.app_context():
        db.create_all()

    return app
