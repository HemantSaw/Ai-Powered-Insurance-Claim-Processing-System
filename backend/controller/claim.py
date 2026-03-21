from flask import request, Blueprint, jsonify
from services.claim_service import create_claim
from utils.auth_util import require_role
from models.claims_model import Claim

claim_bp = Blueprint("claim_bp", __name__, url_prefix="/claim")

@claim_bp.route('/create-claim', methods=["POST"])
@require_role("USER") # I will get current_user from this protected decorator.
def claim(current_user):
    # paitien_name
    # "admission_date",
    # "discharge_date",
    # "diagnosis",
    # claimed_amount,
    data = request.get_json(silent=True)
    patient_name = data["patient_name"]
    policy_id = data['policy_id']
    claimed_amount = data['claimed_amount']
    diagnosis = data['diagnosis']
    admission_date = data['admission_date']
    discharge_date = data['discharge_date']

    metadata = {
        "patient_name" : patient_name,
        "policy_id" : policy_id,
        "diagnosis" : diagnosis,
        "claimed_amount" : claimed_amount,
        "admission_date":admission_date,
        "discharge_date":discharge_date
    }
    return create_claim(metadata=metadata, current_user=current_user)

@claim_bp.route('/get-claims', methods=['GET'])
@require_role("USER")
def get_my_claims(current_user):
    claims = Claim.query.filter_by(created_by=current_user.id).all()
    claims_list = [
            {
                "claim_id": c.claim_id,
                "status": c.status,
                "created_at": c.created_at.isoformat(),
                "form_data": c.form_data
            }
            for c in claims
        ]
    return jsonify(message="claims fetched successfully", status = True, claims_list=claims_list)

@claim_bp.route("get-claim-by-id/<int:claim_id>", methods =['GET'])
@require_role("USER", "HOSPITAL", "APPROVER")
def get_claim_by_id(current_user,claim_id):
    claim = Claim.query.filter_by(claim_id=claim_id).first()
    if not claim:
        return jsonify(message="No Claim Found", status=True), 200
    
    claim_obj = {
                "claim_id": claim.claim_id,
                "status": claim.status,
                "created_at": claim.created_at.isoformat(),
                "form_data": claim.form_data,
                "user_id" : claim.created_by,
                "claimed_amount" : claim.claimed_amount,
                "extracted_data" : claim.extracted_data,
                "evaluation_result": claim.evaluation_result,
                "policy_decision" : claim.policy_decision
            }
    return jsonify(message="Claim fethched successfully", status = True, claim=claim_obj), 200

@claim_bp.route("/get-all-claims", methods = ['GET'])
@require_role("USER", "HOSPITAL", "APPROVER")
def allClaims(current_user):
    claims = Claim.query.all()
    if not claims:
        return jsonify(message="No Claim Found", status=True), 200
    
    claim_list = [{
                "claim_id": claim.claim_id,
                "status": claim.status,
                "created_at": claim.created_at.isoformat(),
                "form_data": claim.form_data,
                "user_id" : claim.created_by,
                "claimed_amount" : claim.claimed_amount,
                "extracted_data" : claim.extracted_data,
                "evaluation_result": claim.evaluation_result,
                "policy_decision" : claim.policy_decision
            } for claim in claims]
    
    return jsonify(message="Claim fethched successfully", status = True, claim_list=claim_list), 200
