from flask import Flask
from flask_jwt_extended import JWTManager
from models import db
from auth.auth import auth_bp
from tasks.tasks import tasks_bp
from config.config import Config

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # Initialize extensions
    db.init_app(app)
    jwt = JWTManager(app)

    # Register blueprints
    app.register_blueprint(auth_bp, url_prefix='/auth')
    app.register_blueprint(tasks_bp, url_prefix='/tasks')

    return app

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)
