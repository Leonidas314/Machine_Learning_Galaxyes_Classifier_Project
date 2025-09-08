from flask import Flask
from .db import db, migrate

def create_app():
    app = Flask(__name__)

    # Configuraciones DB
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///instance/database.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # Inicializar extensiones
    db.init_app(app)
    migrate.init_app(app, db)

    # Importar rutas y registrarlas
    from .routes import api_bp
    app.register_blueprint(api_bp, url_prefix='/api')

    return app
