from extensions import db
from datetime import datetime

class Sprint(db.Model):
    __tablename__ = "sprints"
    sprint_id = db.Column(db.Integer, primary_key=True)
    project_id = db.Column(db.Integer, db.ForeignKey("projects.project_id"), nullable=False)
    name = db.Column(db.String(100), nullable=False)
    date_created = db.Column(db.Date, default=datetime.utcnow)
    deadline = db.Column(db.Date, nullable=False)

    # Relationships
    project = db.relationship('Project', back_populates='sprints')
    tasks = db.relationship('Task', backref='sprint', lazy=True)
