from db import db
from datetime import datetime, timezone

class PolicyAccount(db.Model):
    __tablename__ = "policy_accounts"

    id = db.Column(db.Integer, primary_key=True)

    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False, unique=True)
    policy_id = db.Column(db.Integer, db.ForeignKey("policies.policy_id"), nullable=False)

    total_sum_insured = db.Column(db.Float, nullable=False)
    used_amount = db.Column(db.Float, default=0.0)
    remaining_amount = db.Column(db.Float, nullable=False)

    created_at = db.Column(db.DateTime, default=lambda: datetime.now(timezone.utc))
