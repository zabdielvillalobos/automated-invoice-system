from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

# Initialize the database
db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config.from_object('config.Config')

    # Initialize the database with the app
    db.init_app(app)

    # Set up the login manager
    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'  # The route for logging in
    login_manager.init_app(app)

    # Load the user by ID for Flask-Login
    from .models import User
    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    # Register the blueprints for authentication and the main routes
    # Importing blueprints after app and db initialization to avoid circular import
    from .auth import auth as auth_blueprint
    from .routes import main as main_blueprint

    app.register_blueprint(main_blueprint)
    app.register_blueprint(auth_blueprint)

    return app