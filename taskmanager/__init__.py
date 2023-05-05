import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
# To use hidden file path.
if os.path.exists("env.py"):
    import env  # noqa

# Create an instance for Flask - app.
app = Flask(__name__)
# Set to environment variable.
app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY")
app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("DB_URL")

# Create an instance for SQLAlchemy
db = SQLAlchemy(app)

# Defined after the routed variables above.
from taskmanager import routes  # noqa
