from flask import Flask, request
from flask_restful import Resource, Api, reqparse
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity
from pymongo import MongoClient
from bson import ObjectId



from resources.users import UserRegistration, UserLogin, AllUsers
from resources.notes import NoteResource, NoteCreateResource


# User Schema
user_schema = {
    'name': str,
    'username': str,
    'password': str,
}

# Note Schema
note_schema = {
    'title': str,
    'content': str,
    'user_id': str,
}

app = Flask(__name__)

app.config['JWT_SECRET_KEY'] = 'your-secret-key'
jwt = JWTManager(app)
api = Api(app)

# User registration endpoint
api.add_resource(UserRegistration, '/register')

# User authentication endpoint
api.add_resource(UserLogin, '/login')

# Endpoint to view all registered users (for demonstration purposes)
api.add_resource(AllUsers, '/users')


# Create, Read, Update, Delete (CRUD) operations for notes
# Read, Update, Delete 
api.add_resource(NoteResource, '/notes/<string:note_id>')

# Create
api.add_resource(NoteCreateResource, '/notes')


if __name__ == '__main__':
    app.run(debug=True)
