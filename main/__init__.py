from flask import Flask
from .routes import init_routes
import os

def create_app():
    app = Flask(__name__)
    app.config.from_mapping(
        secret_key="Gc40>x1uwIvNms£868E4gQL",
        DATABASE=os.path.join(app.instance_path, "hazelremmen.sqlite"),
    )
    
    init_routes(app)  # register routes
    
    from . import db
    db.init_app(app)
    
    from . import auth
    app.register_blueprint(auth.bp) # adds the routes defined in the blueprint from base "auth".
    
    return app

# Optional: for WSGI directly
application = create_app()