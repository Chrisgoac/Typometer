from database import db
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship

class Register(db.Model):
    __tablename__ = "regitsters"
    id = db.Column(db.Integer, primary_key=True)
    wpm = db.Column(db.Integer, nullable=False)
    seconds = db.Column(db.Integer, required=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)