from flask import render_template
from random import random

def init_routes(app):
    @app.route('/')
    def index():
        return render_template("base.html", random_num=random(), main_content="blog")