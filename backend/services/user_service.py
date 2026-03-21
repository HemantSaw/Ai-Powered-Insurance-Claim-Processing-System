from flask import jsonify, current_app
from flask_bcrypt import Bcrypt
from db import db
from models.user_model import UserModel
from models.role_model import Role
from datetime import datetime, timedelta, timezone
import jwt, os
from dotenv import load_dotenv

load_dotenv()

bcrypt = Bcrypt()
def set_password(password):
    return bcrypt.generate_password_hash(password).decode("utf-8")

def check_password(raw_password):
    return bcrypt.check_password_hash(set_password(raw_password), raw_password)

def register_user(username, password, email):
    role = "USER"
    if not username and not password and not email and not role:
        return jsonify(message="missing fields. Please fill all the fields", status= False), 400
    
    role_model = Role.query.filter_by(name=role.upper()).first()
    query = UserModel.query.filter_by(email=email).first()
    if not role_model:
        return jsonify(error="Invalid role", status= False), 400
    if query:
        return jsonify(message="user already exists.", status= False),400
    
    user = UserModel(
        username=username,
        email=email,
        role_id=role_model.id
    )

    hash_pass = set_password(password=password)
    print("hash_pass ", hash_pass)
    user.password_hash = hash_pass
    db.session.add(user)
    db.session.commit()

    return jsonify(message="User registered successfully", status=True), 201

def login_user(username, password):
    user = UserModel.query.filter(UserModel.username==username).first()
    if not user or not check_password(raw_password=password):
        return jsonify(message="Invalid email or password ", status= False), 401
    
    payload = {
        "user_id": user.id,
        "role": user.role.name,
        "exp": datetime.now(timezone.utc) + timedelta(hours=1)
    }
    token = jwt.encode(payload, current_app.config["SECRET_KEY"] , algorithm="HS256")

    return jsonify(message="logged in", status= True, token=token, role=user.role.name),200

def change_role_service(user_id, role_name):
    role = Role.query.filter_by(name = role_name).first()
    if not role:
        return jsonify(message = "Invalid role", status=False),400
    
    role_id = role.id
    user = UserModel.query.filter_by(id=user_id).first()
    if not user:
        return jsonify(message = "User not found", status = False), 400
    
    if user.role_id == role_id:
        return jsonify(message="Role already present", status= False), 400
    
    user.role_id = role_id
    db.session.commit()

    return jsonify(message="Role updated successfully", status = True, user_id=user_id, new_role=role_name),200

    
