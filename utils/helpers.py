import re
import itertools
from extensions import db
from models.role import Role
from models.group import Group

# Validation regex
EMAIL_REGEX = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
PHONE_REGEX = r'^\+?1?\d{9,15}$'
VALID_ROLES = ['admin', 'developer', 'manager', 'viewer']

def validate_email(email):
    return re.match(EMAIL_REGEX, email) is not None

def validate_phone(phone):
    return phone is None or re.match(PHONE_REGEX, phone) is not None

def validate_password(password):
    return len(password) >= 8 and re.search(r'[A-Za-z]', password) and re.search(r'\d', password)

def validate_roles(roles):
    return all(role in VALID_ROLES for role in roles)

def generate_role_combinations():
    roles = VALID_ROLES
    combinations = []
    for r in range(1, len(roles) + 1):
        for combo in itertools.combinations(roles, r):
            combinations.append(list(combo))
    return combinations

def initialize_roles_and_groups():
    if not Role.query.first():
        for role_name in VALID_ROLES:
            role = Role(name=role_name)
            db.session.add(role)
        db.session.commit()

    if not Group.query.first():
        combinations = generate_role_combinations()
        for i, combo in enumerate(combinations, 1):
            role = Role.query.filter_by(name=combo[0]).first()
            group_name = '+'.join(combo)
            group = Group(group_id=i, name=group_name, role_id=role.role_id)
            db.session.add(group)
        db.session.commit()