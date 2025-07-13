from flask import request, Blueprint, jsonify
from flask_login import login_required, current_user
from extensions import db
from models.project import Project
from models.team import Team
from utils.decorators import role_required

project_bp = Blueprint("project", __name__)

@project_bp.route('/createprojects', methods=['POST'])
@login_required
@role_required('Admin','Manager')

def create_project():
    data = request.json

    
    if 'name' not in data or 'team_name' not in data:
        return jsonify({'error': 'Project name and team name are required.'}), 400

    
    team = Team.query.filter_by(name=data['team_name']).first()
    if not team:
        return jsonify({'error': f"Team '{data['team_name']}' not found."}), 404


    manager_user_id = current_user.user_id

    new_project = Project(
        name=data['name'],
        description=data.get('description'),
        team_id=team.team_id,
        manager_user_id=manager_user_id,
        start_date=data.get('start_date'),
        end_date=data.get('end_date'),
        status=data.get('status')
    )
    db.session.add(new_project)
    db.session.commit()
    return jsonify({'message': 'Project created', 'project_id': new_project.project_id}), 201
