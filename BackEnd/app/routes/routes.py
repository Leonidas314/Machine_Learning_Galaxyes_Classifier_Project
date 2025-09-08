from flask import Blueprint, jsonify, request, current_app
from ..services.response_service import response_service
from ..services.validation_service import validate_image

#prefijo comun para las rutas de la API
api_bp = Blueprint ("api", __name__)

@api_bp.route("/classify", methods=["POST"])
def classify():
    if "image" not in request.files:
        return jsonify({"error": "no image provided"}), 400
    image = request.files["image"]
    
    #Add MIME type check, extension check and/or image verification by processing
    valid, message = validate_image(image)
    if not valid:
        return jsonify({"error": message}), 400
    
    image128 = image.resize((128,128))

    com_service = current_app.config["COM_SERVICE"]
    category = com_service.process(image128)
    text = response_service(category)
    
    return jsonify({category:text}), 200

#----Server response Test---- 
@api_bp.route("/health", methods=["GET"])
def health():
    return jsonify({"status": "ok"}), 200
