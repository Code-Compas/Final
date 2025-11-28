import os
import shutil
from flask import Flask
from application.database import db
from application.config import LocalDevlopmentConfig


def create_app():
    # serve templates from `templates/` and static from `static/`
    app = Flask(__name__, template_folder="templates", static_folder="static")

    # load default (development) config
    app.config.from_object(LocalDevlopmentConfig)

    # If running on Vercel or in production, use writable /tmp for SQLite
    if os.getenv("VERCEL") or os.getenv("ENV") == "production":
        # prefer an existing checked-in DB if present, copy it to /tmp where it's writable
        repo_db = os.path.join(os.path.dirname(__file__), "..", "db_directory", "projectdb.db")
        tmp_db = "/tmp/projectdb.db"
        try:
            if os.path.exists(repo_db):
                shutil.copyfile(repo_db, tmp_db)
        except Exception:
            # fail silently and let SQLAlchemy create a fresh DB in /tmp
            pass

        app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:////{tmp_db.lstrip('/')}"

    db.init_app(app)

    # ensure tables are created when the app starts (safe for dev & serverless cold starts)
    with app.app_context():
        db.create_all()

    return app


app = create_app()

# Keep an application context active while modules that register routes import.
# `application.controlers` uses `current_app` at import time to decorate routes,
# so push the app context before importing it.
app.app_context().push()

from application.controlers import *


if __name__ == "__main__":
    app.debug = True
    app.run(port=5000)