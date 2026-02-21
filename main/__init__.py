from flask import Flask
from .routes import init_routes

def create_app():
    app = Flask(__name__)
    init_routes(app)  # register routes
    
    from . import auth
    
    app.register_blueprint(auth.bp)
    
    return app

# Optional: for WSGI directly
application = create_app()