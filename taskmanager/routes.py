from flask import render_template
# app, db variable defined in __init__.py file.
from taskmanager import app, db
from taskmanager.models import Category, Task

# Create app route using '/'


@app.route("/")
def home():
    return render_template("tasks.html")


@app.route("/categories")
def categories():
    return render_template("categories.html")


@app.route("/add_category", methods=["GET", "POST"])
def add_category():
    return render_template("add_category.html")
