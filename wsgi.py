#wsgi.py
from app import app, db  # or from thevikidtruth import app

with app.app_context():
    db.create_all()

application = app

