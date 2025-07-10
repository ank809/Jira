from extensions import db
class Team(db.Model):
    __tablename__= "teams"
    team_id= db.Column(db.Integer, primary_key=True)
    user_id= db.Column(db.Integer)

