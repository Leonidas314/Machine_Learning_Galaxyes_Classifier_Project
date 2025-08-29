from flask import Flask
from flask_cors import CORS
from .routes.routes import api_bp

def create_app():
    app = Flask(__name__)
    
    #Enables cross-origin resource sharing (get requests from Frontend)
    CORS(app)
    
    #Register a blueprint on the application (routes) 
    app.register_blueprint(api_bp)
    
    return app