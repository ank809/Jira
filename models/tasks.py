from extensions import db
from datetime import datetime

class Tasks(db.Model):
    __tablename__= "tasks"
    task_id= db.Column(db.Integer, primary_key=True)
    name= db.Column(db.String, nullable=False)
    description= db.Column(db.String, nullable=False)
    project_id= db.Column(db.Integer,db.ForeignKey("projects.project_id"))
    sprint_id= db.Column(db.Integer, db.ForeignKey("sprints.sprint_id"))
    assigned_to= db.Column(db.String,db.ForeignKey("users.user_id"), nullable=False)
    priority= db.Column(db.String, nullable=False)
    type= db.Column(db.String, nullable=False)
    project = db.relationship('Project', backref='tasks')

   