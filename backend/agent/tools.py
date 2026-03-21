from db import db
from langchain.tools import tool
from models.claims_model import Claim
from models.policy_user_map_model import PolicyAccount
from services.text_extraction_service import TextExtractionService
from services.claim_service import evaluate_claim_service
from services.policy_decision_service import policy_decision_service

@tool
def text_extraction(claim_id : int):
    """
    Extracts the details of the patient using the claim_id. 
    This details are from the uploaed document.
    Returns a json object. 
    """
    extracted_object = TextExtractionService.text_extraction_service(claim_id=claim_id) 
    return extracted_object

@tool
def evaluation_result(claim_id : int):
    """
    Evaluates the claim using the claim id on the basis of extracted_data and form_data.
    Returns Final message json that has the result of the evaluation.
    """
    result = evaluate_claim_service(claim_id=claim_id)
    return result

@tool
def policy_check(claim_id : int):
    """
    Checks the policy and Decides if the claim is covered by the policy using the claim_id.
    it returns the Policy decision json which consists the reason of the decision, the decisiion, the recommended next action.

    """
    decision = policy_decision_service(claim_id=claim_id)
    return decision

@tool
def get_claim_context(claim_id: int):
    """
    Gets claim context.
    Returns full context of a claim including:
    - form_data
    - extracted_data
    - evaluation_result
    - policy_decision
    """
    claim = Claim.query.get(claim_id)
    if not claim:
        return {"error": "Claim not found"}

    return {
        "user_id" : claim.created_by,
        "claimed_amount": claim.claimed_amount,
        "form_data": claim.form_data,
        "extracted_data": claim.extracted_data,
        "evaluation_result": claim.evaluation_result,
        "policy_decision": claim.policy_decision
    }

@tool 
def check_balance(user_id: int):
    """checks weather the user has the policy or not and checks the balance of the user"""
    account = PolicyAccount.query.filter_by(user_id=user_id).first()
    if not account:
        return {"has_policy": False}
    print("remaining amount", account.remaining_amount)
    return {
        "has_policy": True,
        "remaining_amount": account.remaining_amount
    }

@tool
def move_to_review(claim_id: int):
    """changs the status of the claim to under review"""
    claim = Claim.query.filter_by(claim_id=claim_id).first()
    claim.status = "UNDER_REVIEW"
    db.session.commit()
    return {"status": "UNDER_REVIEW"}

@tool
def reject_claim(claim_id: int, reason: str):
    """Rejects the claim"""
    claim = Claim.query.get(claim_id)
    claim.status = "REJECTED"
    db.session.commit()
    return {"status": "REJECTED","reason":reason}

@tool
def send_to_human(claim_id: int):
    """Send the claim to human review"""
    claim = Claim.query.get(claim_id)
    claim.status = "PENDING_HUMAN_REVIEW"
    db.session.commit()
    return {"status": "PENDING_HUMAN_REVIEW"}