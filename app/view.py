from app import app
from flask import render_template

@app.route('/')
def index():
    user_name = "Inve"
    return render_template("index.html", name = user_name)