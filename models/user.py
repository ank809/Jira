from extensions import db
from flask_login import UserMixin

class User(db.Model, UserMixin):
    __tablename__ = 'users'
    user_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(255), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)
    phone_number = db.Column(db.String(20))
    group_id = db.Column(db.Integer, db.ForeignKey('groups.group_id'))
    team_id = db.Column(db.Integer, db.ForeignKey("teams.team_id"))

    # Relationships
    group = db.relationship('Group', backref='users')
    team = db.relationship('Team', backref='members')  # 'members' will be a list of users on Team

    @property
    def id(self):
        return self.user_id
