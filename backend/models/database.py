from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def init_db(app):
    db.init_app(app)
    with app.app_context():
        db.create_all()
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Subscription(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)

    def __init__(self, email):
        self.email = email

def init_db(app):
    db.init_app(app)
    with app.app_context():
        db.create_all()
