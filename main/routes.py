from flask import render_template
from random import random

class user:
    def __init__(self):
        self.logged_in=False
        self.name=""
        self.id=""

def init_routes(app):
    @app.route('/')
    def index():
        return render_template("base.html", main_content="blog", user=user, blog_posts=["001","002","003","004"], random_num=random())
    
    @app.route('/motd')
    def motd():
        return render_template("base.html", main_content="motd", user=user)
    
    # @app.route('/auth/login', methods=("GET", "POST"))
    # def login():
    #     return render_template("base.html", main_content="auth/login", user=user)
    
    # @app.route('/auth/register', methods=("GET", "POST"))
    # def register():
    #     return render_template("base.html", main_content="auth/register", user=user)
    
    
    
    
    
    