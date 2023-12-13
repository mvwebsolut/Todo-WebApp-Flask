from configs import DebugConfig
from app import create_app

config = DebugConfig()
app = create_app(config)

if __name__ == "__main__":
    app.run()
