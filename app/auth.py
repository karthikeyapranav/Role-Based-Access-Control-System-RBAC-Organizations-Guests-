from flask import Blueprint, request, jsonify, render_template, redirect, session
from .models import User
from . import db
from flask_jwt_extended import create_access_token
from flask import session

auth_bp = Blueprint("auth", __name__)


@auth_bp.route('/signup', methods=['GET', 'POST'])
def signup_html():  # 🔁 CHANGED name from `signup` to `signup_html`
    if request.method == 'POST':
        username = request.form.get("username")
        email = request.form.get("email")
        password = request.form.get("password")

        if User.query.filter_by(username=username).first():
            return "Username exists"
        user = User(username=username, email=email)
        user.set_password(password)
        db.session.add(user)
        db.session.commit()
        return redirect("/login")

    return render_template("signup.html", title="Sign Up")

@auth_bp.route('/login', methods=['GET', 'POST'])
def login_html():
    if request.method == 'POST':
        username = request.form.get("username")
        password = request.form.get("password")

        user = User.query.filter_by(username=username).first()
        if user and user.check_password(password):
            session['user_id'] = user.id  # ✅ Save user ID in session
            return redirect("/dashboard")
        else:
            return "Invalid Credentials"
    return render_template("login.html", title="Login")