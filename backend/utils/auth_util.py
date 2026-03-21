import jwt
from flask import request, current_app
from models.user_model import UserModel

def get_current_user():
    auth = request.headers.get("Authorization")

    if not auth or not auth.startswith("Bearer "):
        return None

    token = auth.split(" ")[1]

    try:
        data = jwt.decode(token, current_app.config["SECRET_KEY"], algorithms=["HS256"])
    except Exception:
        return None

    return UserModel.query.get(data["user_id"])


def require_role(*roles):
    def decorator(func):
        def wrapper(*args, **kwargs):
            user = get_current_user()
            if not user or user.role.name not in roles:
                return {"error": "Forbidden"}, 403
            return func(user, *args, **kwargs)
        wrapper.__name__ = func.__name__
        return wrapper
    return decorator
