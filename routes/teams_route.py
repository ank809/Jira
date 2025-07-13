from flask import Blueprint, request, jsonify
from flask_login import login_required
from extensions import db
from models.team import Team
from models.user import User
from utils.decorators import role_required

team_bp = Blueprint('team', __name__)

@team_bp.route('/create', methods=['POST'])
@login_required
@role_required('Manager', 'Admin')
def create_team_and_assign_users():
    data = request.json
    name = data.get('name')
    user_ids = data.get('user_ids', [])

    # Validate team name
    if not name:
        return jsonify({'error': 'Team name is required.'}), 400

    # Create the team
    team = Team(name=name)
    db.session.add(team)
    db.session.flush()  # So team.team_id is available before commit

    # Gather users by IDs or emails
    users = []
    if user_ids:
        users = User.query.filter(User.user_id.in_(user_ids)).all()

    # Assign users to the team
    for user in users:
        user.team_id = team.team_id

    db.session.commit()

    return jsonify({
        'message': f'Team "{team.name}" created and {len(users)} users assigned.',
        'team_id': team.team_id
    }), 201
