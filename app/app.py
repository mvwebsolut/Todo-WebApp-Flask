from flask import Flask
from importlib import import_module
from .extensions import database, login_manager, migrate

def create_app(config):
    app = Flask(__name__)
    app.config.from_object(config)

    init_extensions(app)
    register_blueprint(app)

    return app


def init_extensions(app: Flask):
    database.init_app(app)
    login_manager.init_app(app)
    migrate.init_app(app, database)


def register_blueprint(app: Flask):
    for module_name in app.config['BLUEPRINTS']:
        module = import_module(f"app.blueprints.{module_name}")
        app.register_blueprint(module.blueprint)