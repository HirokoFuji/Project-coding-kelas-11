from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import Config

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # Initialize database
    db.init_app(app)
    
    # Import models to ensure they are registered with SQLAlchemy
    from app.models.models import Schedule, Category, Product
    
    # Create database tables
    with app.app_context():
        # Drop all tables first to ensure clean state
        db.drop_all()
        # Create all tables
        db.create_all()
        print("Database tables created successfully!")

    # Register blueprints
    from app.controllers.schedule_controller import schedule_bp
    app.register_blueprint(schedule_bp)  # Remove url_prefix to make it the root route

    return app
