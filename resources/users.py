from flask_restful import Resource, reqparse
from flask_jwt_extended import create_access_token

from db import users_collection
from passlib.hash import pbkdf2_sha256

class UserRegistration(Resource):
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('name', required=True, help="Name field is required.")
        parser.add_argument('username', required=True, help="Username field is required.")
        parser.add_argument('password', required=True, help="Password field is required.")
        data = parser.parse_args()

        if users_collection.find_one({'username': data['username']}):
            return {'message': 'Username already exists. Choose a different username.'}, 400

        hashed_password = pbkdf2_sha256.hash(data["password"])

        user = {
            'name': data['name'],
            'username': data['username'],
            'password': hashed_password, 
        }
        users_collection.insert_one(user)
        return {'message': 'User registered successfully.'}, 201
    

class UserLogin(Resource):
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('username', required=True, help="Username field is required.")
        parser.add_argument('password', required=True, help="Password field is required.")
        data = parser.parse_args()

        user = users_collection.find_one({'username': data['username']})
        if user:
            if pbkdf2_sha256.verify(data['password'], user['password']):
                access_token = create_access_token(identity={'username': user['username']})
                return {'access_token': access_token}, 200
            else:
                return {'message': 'Invalid password'}, 401
        else:
            return {'message': 'User not found'}, 404
        
class AllUsers(Resource):
    def get(self):
        all_users = users_collection.find({}, {'password': 0})
        users = []
        for user in all_users:
            user['_id'] = str(user['_id'])  # Convert ObjectId to string
            users.append(user)
        return {'users': users}, 200