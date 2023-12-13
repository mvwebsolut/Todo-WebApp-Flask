class DebugConfig:
    
    SECRET_KEY = "mateus@123"
    SQLALCHEMY_DATABASE_URI = "sqlite:///debug.db"
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    BLUEPRINTS = [
        "auth",
        "home"
    ]