from flask import jsonify
import uuid
from models.claims_model import Claim
from datetime import datetime, timezone
from db import db

from services.claim_evaluator_engine import ClaimEvaluationEngine

def create_claim(metadata:dict, current_user):
    curr_time = datetime.now(timezone.utc)
    # claim = {
    #     "claim_id": claim_id,
    #     "status": "CREATED",
    #     "created_at": curr_time,
    #     "metadata": metadata
    # }
    print("metadata...", metadata)
    claim = Claim(
        created_by=current_user.id,
        claimed_amount=metadata.get("claimed_amount"),
        policy_id=metadata.get("policy_id"),
        status="CREATED",
        created_at = curr_time,
        form_data = metadata
    )
    db.session.add(claim)
    db.session.commit()
    return jsonify(message="claim created successfully", status = True, claim_id=claim.claim_id), 200

def evaluate_claim_service(claim_id):
    claim = Claim.query.get(claim_id)
    if not claim:
        return jsonify(message = "Claim not found", status = False), 404
    
    extracted_data = claim.extracted_data

    if not claim.form_data or not claim.extracted_data:
        return jsonify(message = "Claim form data or extracted data missing", status = False), 400
    
    evaluation = ClaimEvaluationEngine.evaluate(
        form_data=claim.form_data,
        extracted_data=claim.extracted_data
    )

    claim.evaluation_result = evaluation
    db.session.commit()
    return evaluation

    # return jsonify(
    #     message="Claim evaluated",
    #     status=True,
    #     evaluation=evaluation
    # ), 200

    

