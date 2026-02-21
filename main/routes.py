from flask import render_template
from random import random

def init_routes(app):
    @app.route('/')
    def index():
        return render_template("base.html", main_content="blog", random_num=random())
    
    @app.route('/MOTD')
    def index():
        return render_template("base.html", main_content="motd")