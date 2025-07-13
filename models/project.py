from extensions import db
from datetime import datetime
class Project(db.Model):
    __tablename__ = "projects"
    project_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), nullable=False)
    description = db.Column(db.Text)
    team_id = db.Column(db.Integer, db.ForeignKey("teams.team_id"), nullable=False)
    manager_user_id = db.Column(db.Integer, db.ForeignKey("users.user_id"), nullable=False)
    start_date = db.Column(db.Date)
    end_date = db.Column(db.Date)
    status = db.Column(db.String(50))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    # Relationships
    sprints = db.relationship('Sprint',back_populates='project')
    tasks = db.relationship('Task', backref='project', lazy=True)
    team = db.relationship('Team', backref='projects')
    manager = db.relationship('User', foreign_keys=[manager_user_id], backref='managed_projects')