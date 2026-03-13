from flask import Blueprint
from flask_restful import Api
from app.app import UserList, SingleUser, NewUser, DeleteUser, UpdateUser

api_bp = Blueprint('api', __name__)
api = Api(api_bp)

# Define the routes and link them to the resource classes
api.add_resource(UserList, '/')
api.add_resource(SingleUser, '/<int:num>')
api.add_resource(NewUser, '/user')
api.add_resource(DeleteUser, '/delete/<int:num>')
api.add_resource(UpdateUser, '/update/<int:id>')

def init_routes(app):
    app.register_blueprint(api_bp, url_prefix='/api')