from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_migrate import Migrate

database = SQLAlchemy()
login_manager = LoginManager()
migrate = Migrate()