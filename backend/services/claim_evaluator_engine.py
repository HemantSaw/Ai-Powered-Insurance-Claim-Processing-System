from flask import jsonify

class ClaimEvaluationEngine:

    @staticmethod
    def evaluate(form_data: dict, extracted_data: dict):
        reasons = []
        risk_flags = [] 

        required_fields = [
            "admission_date",
            "discharge_date",
            "diagnosis",
            "total_bill_amount"
        ]

        missing_fields = []

        for field in required_fields:
            if not extracted_data.get(field):
                missing_fields.append(field)

        if missing_fields:
            reasons.append(f"Missing fields in documents: {missing_fields}")
            msg = {
                "evaluation_result": "INCOMPLETE_INFORMATION",
                "reasons": reasons,
                "risk_flags": [],
                "confidence": "LOW"
            }
            return msg
        
        if form_data.get("patient_name").lower() != extracted_data.get("patient_name").lower():
            reasons.append("Name is different")
            risk_flags.append("NAME_MISMATCH")
        
        if form_data.get("admission_date") != extracted_data.get("admission_date"):
            reasons.append(f"Admission date mismatch between form and documents{form_data.get("admission_date"), extracted_data.get("admission_date")}")
            risk_flags.append("ADMISSION_DATE_MISMATCH")

        if form_data.get("discharge_date") != extracted_data.get("discharge_date"):
            reasons.append(f"Discharge date mismatch between form and documents {form_data.get("discharge_date"),extracted_data.get("discharge_date")}")
            risk_flags.append("DISCHARGE_DATE_MISMATCH")

        try:
            form_amount = float(form_data.get("claimed_amount", 0))
            doc_amount = float(extracted_data.get("total_bill_amount", 0))
            if form_amount - doc_amount > 500:
                reasons.append("Claimed amount significantly differs from document amount")
                risk_flags.append("AMOUNT_MISMATCH")
        except Exception:
            reasons.append("Invalid amount format")
            risk_flags.append("AMOUNT_PARSE_ERROR")

        if risk_flags:
            msg = {
                "evaluation_result": "NEEDS_HUMAN_REVIEW",
                "reasons": reasons,
                "risk_flags": risk_flags,
                "confidence": "MEDIUM"
            }

            return msg
        
        final_msg = {
            "evaluation_result": "CLEAN",
            "reasons": ["All checks passed"],
            "risk_flags": [],
            "confidence": "HIGH"
        }
        return final_msg