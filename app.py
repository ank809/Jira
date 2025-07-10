from flask import Flask, jsonify
from flask_migrate import Migrate
from config import Config
from extensions import db  
from routes.auth_routes import auth_bp
from routes.profile_route import profile_bp
from routes.dashboard_route import dash_bp
from flask_login import LoginManager
from models.user import User

app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)  
migrate = Migrate(app, db)

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'auth.login'  

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

@app.errorhandler(401)
def unauthorized_error(error):
    return jsonify({"error": "User not logged in"}), 401

app.register_blueprint(auth_bp, url_prefix='/auth')
app.register_blueprint(dash_bp, url_prefix='/')
app.register_blueprint(profile_bp, url_prefix='/')

if __name__ == "__main__":
    app.run(debug=True)
