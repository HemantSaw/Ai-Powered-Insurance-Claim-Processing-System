from flask import request, Blueprint, jsonify
from utils.auth_util import require_role
from models.role_model import Role
from models.claims_model import Claim
from db import db
import os

from services.user_service import change_role_service
from services.text_extraction_service import TextExtractionService
from services.claim_service import evaluate_claim_service
from services.policy_decision_service import policy_decision_service
from langchain_core.messages import SystemMessage, HumanMessage

from agent.agent import agent

admin_bp = Blueprint("admin_bp", __name__, url_prefix='/approver')

@admin_bp.route("/users/<int:user_id>/role", methods=["PUT"])
@require_role("APPROVER")
def change_role(current_user, user_id):
    data = request.get_json()
    role_name = data.get('role',"").upper()
    return change_role_service(user_id=user_id, role_name=role_name)

@admin_bp.route("/claim/<int:claim_id>/review", methods=["POST"])
@require_role("APPROVER")
def start_review_claim(current_user, claim_id):
    claim = Claim.query.filter_by(claim_id=claim_id).first()
    if not claim:
        return jsonify(message="Claim not found", status = False), 400
    
    claim.status = "UNDER_REVIEW"
    db.session.commit()

    return jsonify(message="Review has been started", status = True), 200

@admin_bp.route("/claim/<int:claim_id>/decision", methods=["POST"])
@require_role("APPROVER")
def decision_claim(current_user, claim_id):
    data = request.get_json()
    decision = data["decision"]
    reason = data["reason"]

    if decision not in ["APPROVED", "REJECTED"]:
        return jsonify(message = "Decision must be APPROVED or REJECTED", status = False), 400
    
    claim = Claim.query.filter_by(claim_id=claim_id).first()
    if not claim :
        return jsonify(message="Claim not found", status = False), 400
    
    claim.status = decision

    form = claim.form_data or {}
    form["decision_reason"] = reason
    claim.form_data = form

    db.session.commit()
    return jsonify(message = f"claim {decision}", status = True),200

@admin_bp.route("/claim/<int:claim_id>/extract", methods=["POST"])
@require_role("APPROVER")
def extract_claim_data(current_user, claim_id):
    claim = Claim.query.get(claim_id)
    if not claim:
        return jsonify(message = "Claim not found", status= False), 400
    
    return TextExtractionService.text_extraction_service(current_user=current_user, claim_id=claim_id)

@admin_bp.route("/claim/<int:claim_id>/evaluate", methods = ["POST"])
@require_role("APPROVER")
def evaluate_claim(current_user, claim_id):
    
    return evaluate_claim_service(claim_id=claim_id)

@admin_bp.route("/claim/<int:claim_id>/policy-decision", methods=["POST"])
@require_role("APPROVER")
def policy_decision(current_user, claim_id):
    
    return policy_decision_service(claim_id=claim_id)

@admin_bp.route("/claim/<int:claim_id>/agent-act", methods=["POST"])
@require_role("APPROVER")
def run_react_agent(current_user, claim_id):
    user_query = f"Process claim with id {claim_id} and decide next action."
    result = agent.invoke({"messages": [HumanMessage(content=user_query)]})
    ai_message_text = result["messages"][-1].content
    print(ai_message_text)
    return jsonify(message="claim processed successfully", result=ai_message_text, status =True), 200