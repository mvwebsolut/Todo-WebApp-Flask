class DebugConfig:
    
    SECRET_KEY = "supersecret@123"
    SQLALCHEMY_DATABASE_URI = "sqlite:///debug.db"
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    BLUEPRINTS = [
        "auth", #Blueprint de autenticação
        "home" #Blueprint do app
    ]