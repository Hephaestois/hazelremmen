import sys
from main import application
# So that below import can be found
sys.path.insert(0, "/var/www/hazelremmen")

from flask import Flask

def create_app(test_config=None):
    app = Flask(__name__)
    
    app.add_url_rule("/", endpoint="templates/base.html")
    
    return app
    
    
    
