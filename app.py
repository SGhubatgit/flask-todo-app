from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from config import Config

# ================================
# Initialize extensions (NO app yet)
# ================================
db = SQLAlchemy()
bcrypt = Bcrypt()
login_manager = LoginManager()
login_manager.login_view = "auth.login"
login_manager.login_message_category = "info"


# ================================
# Application Factory
# ================================
def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # Bind extensions to app
    db.init_app(app)
    bcrypt.init_app(app)
    login_manager.init_app(app)

    # ----------------
    # Import models
    # ----------------
    from models.user import User
    from models.task import Task

    # ----------------
    # Create tables (SQLite)
    # ----------------
    with app.app_context():
        db.create_all()

    # ----------------
    # Register blueprints
    # ----------------
    from routes.auth_routes import auth_bp
    from routes.task_routes import task_bp
    from routes.main_routes import main_bp

    app.register_blueprint(auth_bp)
    app.register_blueprint(task_bp)
    app.register_blueprint(main_bp)

    return app
