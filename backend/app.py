import os

from flask import Flask, jsonify, request
from flask_cors import CORS

from db import db
from config import Config

from controller.claim import claim_bp
from controller.users import user_bp
from controller.approver import admin_bp
from controller.upload_document import document_bp

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    CORS(app, resources={r"/*": {"origins": "*"}}, allow_headers=["Content-Type", "Authorization"])

    # Why? Database initialization must happen before using models.
    db.init_app(app)

    # Create tables on first run
    from models.role_model import Role
    from models.user_model import UserModel
    from models.claims_model import Claim
    from models.document_model import DocumentModel
    from models.policy_model import PolicyModel
    from models.policy_user_map_model import PolicyAccount
    with app.app_context():
        db.create_all()

    # Register Blueprints
    # app.register_blueprint(user_bp)

    return app

app = create_app()
app.register_blueprint(claim_bp)
app.register_blueprint(user_bp)
app.register_blueprint(admin_bp)
app.register_blueprint(document_bp)

@app.route("/health", methods=["GET"])
def health_check():
    return jsonify({
        "status": "ok",
        "message": "SmartOps AI backend is running"
    })

if __name__ == "__main__":
    # print(health_check())
    app.run(debug=True)