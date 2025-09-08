from pathlib import Path
from flask import Flask
from BackEnd.app.routes import api_bp
from BackEnd.app.ml_engine import MLEngine
from BackEnd.app.services.db_service import DbService
from BackEnd.app.services.file_storage_service import FileStorageService
from BackEnd.app.services.com_service import ComService


# Inicializar Flask
app = Flask(__name__)
app.register_blueprint(api_bp, url_prefix="/api")

# Cargar modelo y servicios
MODEL_PATH = Path(__file__).parent / "model" / "galaxy_model.h5"
ml_engine = MLEngine(str(MODEL_PATH))
db_service = DbService()
storage_service = FileStorageService()
com_service = ComService(ml_engine, db_service, storage_service)

# Guardar la instancia en la app
app.config["COM_SERVICE"] = com_service

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
