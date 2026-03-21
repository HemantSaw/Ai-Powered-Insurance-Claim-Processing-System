from flask import Blueprint, request, jsonify
from flask_cors import CORS
from services.user_service import register_user, login_user

user_bp = Blueprint("user_bp", __name__, url_prefix="/user")
# CORS(user_bp)

@user_bp.route("/register", methods = ["POST"])
def register():
    data = request.get_json(silent=True)
    username = data['username']
    email = data['email']
    password = data['password']
    return register_user(username=username, email=email, password=password)

@user_bp.route("/login", methods = ["POST"])
def login():
    data = request.get_json()
    username = data['username']
    password = data['password']
    return login_user(username=username, password=password)



