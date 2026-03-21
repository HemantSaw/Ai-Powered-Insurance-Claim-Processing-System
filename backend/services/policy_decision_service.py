from flask import jsonify
import uuid, os, json
from models.claims_model import Claim
from datetime import datetime, timezone
from db import db

from agent.text_extraction_agent import Agent

def policy_decision_service(claim_id):
    claim = Claim.query.get(claim_id)
    if not claim:
        return jsonify(message = "Claim not found", status = False), 404
    
    basedir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join('/Users/mr.wolf/Desktop/insurance_claimer/backend', 'policies/abc_health_insurance_policy.txt')

    policy_text = ""
    # Open and read the file content
    try:
        with open(file_path, 'r') as file:
            policy_text = file.read()
    except IOError as e:
        policy_text = f"Error reading file: {e}"

    print(policy_text)
    claim_form_data = json.dumps(claim.form_data)
    claim_extracted_data = json.dumps(claim.extracted_data)
    claim_evaluation_result = json.dumps(claim.evaluation_result)
    policy_decision = Agent.policy_reason_llm(policy_text, claim_form_data, claim_extracted_data, claim_evaluation_result)

    claim.policy_decision = policy_decision
    db.session.commit()
    print("policy_decision", policy_decision)
    return policy_decision

    # return jsonify(
    #     message="Policy reasoning completed",
    #     policy_decision=policy_decision
    # ), 200