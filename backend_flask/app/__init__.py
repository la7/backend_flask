from flask import Flask

def create_app():
    app = Flask(__name__)
    
    # Initialize configurations and extensions here
    from app.models import db
    db.init_app(app)

    # Import and register routes
    from app.routes import api
    api.init_app(app)

    # Initialize Swagger
    from app.swagger import init_swagger
    init_swagger(app)

    return app