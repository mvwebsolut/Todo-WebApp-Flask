from flask import Flask
from importlib import import_module

from .extensions import database, login_manager, migrate
from .custom_filters import completed_tasks_filter, get_list_by_id, get_completed_tasks_from_list

def create_app(config):
    app = Flask(__name__)
    app.config.from_object(config)

    init_extensions(app)
    register_blueprint(app)

    app.jinja_env.filters['completed_tasks_filter'] = completed_tasks_filter
    app.jinja_env.filters['get_list_by_id'] = get_list_by_id
    app.jinja_env.filters['get_completed_tasks_from_list'] = get_completed_tasks_from_list

    return app


def init_extensions(app: Flask):
    database.init_app(app)
    login_manager.init_app(app)
    migrate.init_app(app, database)


def register_blueprint(app: Flask):
    for module_name in app.config['BLUEPRINTS']:
        module = import_module(f"app.blueprints.{module_name}")
        app.register_blueprint(module.blueprint)