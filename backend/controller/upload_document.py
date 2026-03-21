from flask import request, Blueprint, jsonify
from utils.auth_util import require_role
from services.document_service import DocumentService

document_bp = Blueprint("document_bp", __name__, url_prefix='/document')

@document_bp.route("/claims/<claim_id>/documents", methods=['POST'])
@require_role("HOSPITAL", "USER")
def upload(current_user, claim_id):
    file = request.files.get("file")
    if not file :
        return jsonify(message = "file is required", status= False), 400
    
    return DocumentService.upload_document_service(current_user=current_user, claim_id=claim_id, file=file)
    