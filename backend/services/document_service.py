from flask import jsonify
import os
from db import db
import easyocr
from pdf2image import convert_from_path

from models.claims_model import Claim
from models.document_model import DocumentModel

reader = easyocr.Reader(['en'])
class DocumentService:

    @classmethod
    def upload_document_service(cls, current_user, claim_id, file):
        claim = Claim.query.filter_by(claim_id=claim_id).first()
        if not claim:
            return jsonify(message = "Claim not found", status=False), 400
        
        UPLOAD_FOLDER = "uploads"
        os.makedirs(UPLOAD_FOLDER, exist_ok=True)

        filename = f"{claim_id}_{file.filename}"
        filepath = os.path.join(UPLOAD_FOLDER, filename)

        file.save(filepath)

        #-------- OCR steps -----   
        text = ""
        filename = file.filename.lower()
        if filename.endswith((".png", ".jpg", ".jpeg")):
            result = reader.readtext(filepath, detail=0, paragraph=True)
            text = "\n".join(result)

        elif filename.endswith(".pdf"):
            pages = convert_from_path(filepath, dpi=300)

            page_texts = []

            for page in pages:
                page.save("temp_page.jpg", "JPEG")
                result = reader.readtext("temp_page.jpg", detail=0, paragraph=True)
                page_texts.append("\n".join(result))

                text = "\n\n".join(page_texts)

        document = DocumentModel(
            claim_id=claim_id,
            uploaded_by=current_user.id,
            role=current_user.role.name,
            file_path=filepath,
            file_type=file.mimetype,
            ocr_text = text
        )

        db.session.add(document)

        claim.status = "DOCUMENTS_UPLOADED"

        db.session.commit()

        return jsonify(message="Document uploaded successfully", status = True, filepath=filepath, text= text), 201