from flask import Blueprint, jsonify
from utils.auth_util import require_role
from models.claims_model import Claim
from services.claim_service import evaluate_claim_service

evaluate_bp = Blueprint("evaluate_bp", __name__, url_prefix="/evaluate")

@evaluate_bp.route("/claims/<int:claim_id>/evaluate", methods = ["POST"])
@require_role("APPROVER")
def evaluate_claim(current_user, claim_id):
    return evaluate_claim_service(claim_id)