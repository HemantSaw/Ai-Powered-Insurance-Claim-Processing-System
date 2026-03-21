from db import db
from datetime import datetime
import uuid

from models.user_model import UserModel

def generate_uuid():
    return str(uuid.uuid4())

class Claim(db.Model):
    __tablename__ = "claims"

    claim_id = db.Column(db.Integer, primary_key=True)
    policy_id = db.Column(db.Integer, db.ForeignKey("policies.policy_id"), nullable=False)
    claimed_amount = db.Column(db.Float, nullable=False)
    created_by = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    status = db.Column(db.String(50), default="CREATED")
    created_at = db.Column(db.DateTime, default=datetime.now)
    form_data = db.Column(db.JSON, nullable = True)
    user = db.relationship("UserModel",  back_populates="claims")
    extracted_data = db.Column(db.JSON, nullable=True)
    evaluation_result = db.Column(db.JSON, nullable=True)
    policy_decision = db.Column(db.JSON, nullable=True)