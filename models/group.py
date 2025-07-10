from extensions import db

class Group(db.Model):
    __tablename__ = 'groups'
    group_id = db.Column(db.Integer, primary_key=True)
    role_id = db.Column(db.Integer, db.ForeignKey('roles.role_id'), nullable=False)
    role = db.relationship('Role', backref='groups')
