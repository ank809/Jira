from extensions import db
from datetime import datetime

class Task(db.Model):
    __tablename__ = "tasks"
    task_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), nullable=False)
    description = db.Column(db.Text, nullable=False)
    project_id = db.Column(db.Integer, db.ForeignKey("projects.project_id"), nullable=False)
    sprint_id = db.Column(db.Integer, db.ForeignKey("sprints.sprint_id"), nullable=True)  # Nullable for backlog
    assigned_to = db.Column(db.Integer, db.ForeignKey("users.user_id"), nullable=False)
    priority = db.Column(db.String(50), nullable=False)
    type = db.Column(db.String(50), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    # Relationships
    assignee = db.relationship('User', foreign_keys=[assigned_to], backref='tasks')
   