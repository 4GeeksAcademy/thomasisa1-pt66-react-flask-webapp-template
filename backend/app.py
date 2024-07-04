from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from .routes import api
from .admin import setup_admin
from .config import Config

# Initialize extensions
db = SQLAlchemy()
migrate = Migrate()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # Initialize extensions
    db.init_app(app)
    migrate.init_app(app, db)

    # Allow CORS requests to this API
    CORS(app)

    # Register blueprints
    app.register_blueprint(api, url_prefix='/api')
    
    # Set up Flask-Admin
    setup_admin(app)

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)