from flask import Flask, jsonify, request
from flask_restful import Api, Resource
from flask_sqlalchemy import SQLAlchemy
from flasgger import Swagger

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///text.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
swagger = Swagger(app) 

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    dob = db.Column(db.String(80), nullable=False)
    
    def __init__(self, name, dob):
        self.name = name
        self.dob = dob
    
    def __repr__(self):
        return '<Name %r>' % self.name
    
api = Api(app)

class UserList(Resource):
    def get(self):
        """
        Get list of users
        ---
        responses:
          200:
            description: List of users
            schema:
              type: array
              items:
                type: object
                properties:
                  id:
                    type: integer
                  name:
                    type: string
                  dob:
                    type: string
        """
        return jsonify([{
            'id': user.id, 'name': user.name, 'dob': user.dob
            } for user in User.query.all()
        ])
    
class SingleUser(Resource):
    def get(self, num):
        """
        Get a single user by ID
        ---
        parameters:
          - name: num
            in: path
            type: integer
            required: true
        responses:
          200:
            description: User data
            schema:
              type: object
              properties:
                id:
                  type: integer
                name:
                  type: string
                dob:
                  type: string
          404:
            description: User not found
        """
        user = User.query.filter_by(id=num).first_or_404()
        return jsonify([{
            'id': user.id, 'name': user.name, 'dob': user.dob
            }])
        
class NewUser(Resource):
    def post(self):
        """
        Create a new user
        ---
        parameters:
          - name: body
            in: body
            required: true
            schema:
              type: object
              properties:
                name:
                  type: string
                dob:
                  type: string
        responses:
          200:
            description: User created successfully
        """
        try:
            new_x = request.get_json()
            newuser = User(new_x['name'], new_x['dob'])
            db.session.add(newuser)
            db.session.commit()
            return {'message': 'POST data read successfully'}
        except:
            return {'message': 'Something went wrong'}

class DeleteUser(Resource):
    def delete(self, num):
        """
        Delete a user by ID
        ---
        parameters:
          - name: num
            in: path
            type: integer
            required: true
        responses:
          200:
            description: User deleted successfully
          404:
            description: User not found
        """
        try:
            user = User.query.filter_by(id=num).first()
            db.session.delete(user)
            db.session.commit()
            return {'message': 'User successfully deleted'}
        except:
            return {'message': 'Something went wrong'}
        
class UpdateUser(Resource):
    def put(self, id):
        """
        Update a user by ID
        ---
        parameters:
          - name: id
            in: path
            type: integer
            required: true
          - name: body
            in: body
            required: true
            schema:
              type: object
              properties:
                name:
                  type: string
                dob:
                  type: string
        responses:
          200:
            description: User updated successfully
        """
        try:
            user = User.query.filter_by(id=id).first()
            new_x = request.get_json()
            if new_x.get('name'):
                user.name = new_x['name']
            if new_x.get('dob'):
                user.dob = new_x['dob']
            db.session.commit()
            return {'message': 'User successfully updated'}
        except:
            return {'message': 'Something went wrong'}

    def patch(self, id):
        """
        Partially update a user by ID
        ---
        parameters:
          - name: id
            in: path
            type: integer
            required: true
          - name: body
            in: body
            schema:
              type: object
              properties:
                name:
                  type: string
                dob:
                  type: string
        responses:
          200:
            description: User updated successfully
        """
        try:
            user = User.query.filter_by(id=id).first()
            new_x = request.get_json()
            if new_x.get('name'):
                user.name = new_x['name']
            if new_x.get('dob'):
                user.dob = new_x['dob']
            db.session.commit()
            return {'message': 'User successfully updated'}
        except:
            return {'message': 'Something went wrong'}

api.add_resource(UserList, '/')
api.add_resource(SingleUser, '/<int:num>')
api.add_resource(NewUser, '/user')
api.add_resource(DeleteUser, '/delete/<int:num>')
api.add_resource(UpdateUser, '/update/<int:id>')

with app.app_context():
    db.create_all()
    print("Database tables created!")

#init_swagger(app)

if __name__ == '__main__':
    app.run(debug=True)