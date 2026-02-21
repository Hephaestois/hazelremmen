from flask import render_template
from random import random

def init_routes(app):
    @app.route('/')
    def index():
        return render_template("base.html", main_content="blog", blog_posts=["001","002","003","004"])
    
    @app.route('/motd')
    def motd():
        return render_template("base.html", main_content="motd")