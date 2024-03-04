from app import db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin

class Users(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    telephone = db.Column(db.String(50), nullable=False)
    password = db.Column(db.String(50), nullable=False)
    bonus_count = db.Column(db.Integer, nullable=False)
    last_purchase = db.Column(db.String(50), nullable=False)

class Discounts(db.Model):
    __tablename__ = 'discounts'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50), nullable=False)
    description = db.Column(db.String(200), nullable=False)
    
def create_models(app):
    with app.app_context():
        db.create_all()