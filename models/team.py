from extensions import db
from datetime import datetime

class Team(db.Model):
    __tablename__ = "teams"
    team_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False, unique=True)
