from flask import Blueprint
from flask import flash
from flask import request
from flask import g #Globally accessible object
from flask import redirect
from flask import url_for
from flask import render_template
from werkzeug.security import generate_password_hash

# from . import get_db

def get_db(): pass

bp = Blueprint("auth", __name__, url_prefix="/auth")

@bp.route("/register", methods=("GET", "POST"))
def register():
    """
    Generate a new user. 
    If user exists, log them in.
    """
    print("Made it to the function!")
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        db = get_db()
        
        # Feedback for the user
        error = None
        
        if not username:
            error = "A username is required"
        elif not password:
            error = "A password is required"
        
        if error is None:
            try:
                print("User registered!")
                #db.execute(
                #    "INSERT INTO users (username, password) VALUES (?, ?)", (username, generate_password_hash(password))
                #)
            except db.IntegrityError:
                error = f"User {username} already exists!"                
            else:
                return redirect(url_for("auth.register"))
        
        flash(error)
        
    return render_template("auth/register.html")




