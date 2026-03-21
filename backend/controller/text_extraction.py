from flask import Blueprint,jsonify
from utils.auth_util import require_role
from services.text_extraction_service import TextExtractionService
from models.claims_model import Claim

extract_bp = Blueprint("extract_bp", __name__, url_prefix='/extract')

@extract_bp.route("/claims/<int:claim_id>/extract", methods=["POST"])
@require_role("APPROVER")
def extract_claim_data(current_user, claim_id):
    claim = Claim.query.get(claim_id)
    if not claim:
        return jsonify(message = "Claim not found", status= False), 400
    
    return TextExtractionService.text_extraction_service(claim_id=claim_id)