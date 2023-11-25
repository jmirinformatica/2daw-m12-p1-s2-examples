from . import db_manager as db
from flask_login import UserMixin

# Taula items
class Item(db.Model):
    __tablename__ = "items"
    id = db.Column(db.Integer, primary_key=True)
    store_id = db.Column(db.Integer, db.ForeignKey("stores.id"), nullable=False)
    nom = db.Column(db.String, nullable=False)
    unitats = db.Column(db.Integer, nullable=False)

# Taula stores
class Store(db.Model):
    __tablename__ = "stores"
    id = db.Column(db.Integer, primary_key=True)
    nom = db.Column(db.String, nullable=False)

# Taula users
class User(UserMixin, db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String, unique=True, nullable=False)
    role = db.Column(db.String, nullable=False)
    password = db.Column(db.String, nullable=False)

    def get_id(self):
        return self.email