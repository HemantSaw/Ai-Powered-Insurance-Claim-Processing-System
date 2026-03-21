from db import db
from datetime import datetime, timezone

class DocumentModel(db.Model):
    __tablename__ = 'documents'

    id = db.Column(db.Integer, primary_key=True)
    claim_id = db.Column(db.Integer, db.ForeignKey("claims.claim_id"), nullable=False)
    uploaded_by = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    role = db.Column(db.String(20))   # USER or HOSPITAL
    file_path = db.Column(db.String(255), nullable=False)
    file_type = db.Column(db.String(50))
    uploaded_at = db.Column(
        db.DateTime,
        default=lambda: datetime.now(timezone.utc)
    )
    ocr_text = db.Column(db.Text, nullable=True)
