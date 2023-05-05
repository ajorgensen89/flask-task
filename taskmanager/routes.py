from flask import render_template
# app, db variable defined in __init__.py file.
from taskmanager import app, db
from taskmanager.models import Category, Task

# Create app route using '/'


@app.route("/")
def home():
    return render_template("base.html")
