from flask import jsonify
from models.document_model import DocumentModel
from models.claims_model import Claim
import json
from db import db

from agent.text_extraction_agent import Agent

class TextExtractionService():

    @classmethod
    def text_extraction_service(cls, claim_id):
        claim = Claim.query.get(claim_id)
        documents = DocumentModel.query.filter_by(claim_id=claim_id).all()
        ocr_texts = [d.ocr_text for d in documents if d.ocr_text]
        if not ocr_texts:
            return jsonify(message = "No OCR text available", status = False), 400

        combined_text = "\n\n".join(ocr_texts)

        response = Agent.text_extraction_llm(combined_text=combined_text)
        clean_response = response.content.replace("```json","").replace("```","").strip()

        extracted_text = json.loads(clean_response)

        claim.extracted_data = extracted_text
        db.session.commit()
        return extracted_text
        # return jsonify(message="extracted successfully", status = True, extracted_text=extracted_text), 200

        
