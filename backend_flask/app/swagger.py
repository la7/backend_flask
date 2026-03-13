from flask_swagger_ui import get_swaggerui_blueprint
from flask import Blueprint

swaggerui_blueprint = get_swaggerui_blueprint(
    '/swagger',
    'http://localhost:5000/static/swagger.json',
    config={
        'app_name': "Flask API"
    }
)

def init_swagger(app):
    app.register_blueprint(swaggerui_blueprint, url_prefix='/swagger')