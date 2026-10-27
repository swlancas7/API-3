import os

class ProductionConfig:
    DEBUG = False
    TESTING = False
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = os.environ.get('SECRET_KEY')

    # Optional: fail fast if critical secrets are missing
    if not SQLALCHEMY_DATABASE_URI or not SECRET_KEY:
        raise ValueError("DATABASE_URL and SECRET_KEY must be set")

class DevelopmentConfig:
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL', 'sqlite:///mechanic_shop.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = os.environ.get('SECRET_KEY', 'dev-secret')

    def create_app(config_class=None):
    app = Flask(__name__)
    
    if config_class:
        app.config.from_object(config_class)
    else:
        # Fallback for local/dev
        app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', 'sqlite:///mechanic_shop.db')
        app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
        app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'dev-secret')

    db.init_app(app)
    # ... register blueprints, swagger, etc. (same as before)
    return app

from app import create_app
from config import ProductionConfig

app = create_app(ProductionConfig)

# Do NOT include app.run() here

