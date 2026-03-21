from db import db
from datetime import datetime, timezone

class PolicyModel(db.Model):
    __tablename__ = "policies"

    policy_id = db.Column(db.Integer, primary_key=True)
    policy_number = db.Column(db.String(50), unique=True)
    policy_text = db.Column(db.Text)  # full policy wording
    created_at = db.Column(db.DateTime, default=lambda: datetime.now(timezone.utc))