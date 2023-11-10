# from flask import Flask, request
# from flask_restful import Resource, Api, reqparse
# from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity
# from pymongo import MongoClient

# app = Flask(__name__)
# app.config['JWT_SECRET_KEY'] = 'your-secret-key'
# api = Api(app)
# jwt = JWTManager(app)

# # Set up MongoDB connection
# client = MongoClient('mongodb://localhost:27017/')
# db = client['NoteApp']
# users_collection = db['users']
# notes_collection = db['notes']

# # User Schema
# user_schema = {
#     'name': str,
#     'username': str,
#     'password': str,
# }

# # Note Schema
# note_schema = {
#     'title': str,
#     'content': str,
#     'user_id': str,
# }

# # User registration endpoint
# class UserRegistration(Resource):
#     def post(self):
#         parser = reqparse.RequestParser()
#         parser.add_argument('name', required=True, help="Name field is required.")
#         parser.add_argument('username', required=True, help="Username field is required.")
#         parser.add_argument('password', required=True, help="Password field is required.")
#         data = parser.parse_args()

#         if users_collection.find_one({'username': data['username']}):
#             return {'message': 'Username already exists. Choose a different username.'}, 400

#         user = {
#             'name': data['name'],
#             'username': data['username'],
#             'password': data['password'],  # You should hash the password before storing it
#         }
#         users_collection.insert_one(user)
#         return {'message': 'User registered successfully.'}, 201

# api.add_resource(UserRegistration, '/register')

# # User authentication endpoint
# class UserLogin(Resource):
#     def post(self):
#         parser = reqparse.RequestParser()
#         parser.add_argument('username', required=True, help="Username field is required.")
#         parser.add_argument('password', required=True, help="Password field is required.")
#         data = parser.parse_args()

#         user = users_collection.find_one({'username': data['username'], 'password': data['password']})
#         if user:
#             access_token = create_access_token(identity={'username': user['username']})
#             return {'access_token': access_token}, 200
#         return {'message': 'Invalid credentials'}, 401

# api.add_resource(UserLogin, '/login')

# # Endpoint to view all registered users (for demonstration purposes)
# class AllUsers(Resource):
#     @jwt_required()
#     def get(self):
#         current_user = get_jwt_identity()
#         # if current_user['username'] == 'admin':  # Example admin check
#         all_users = users_collection.find({}, {'_id': 0, 'password': 0})
#         users = [user for user in all_users]
#         return {'users': users}, 200
#         return {'message': 'Access denied'}, 403

# api.add_resource(AllUsers, '/users')

# # Create, Read, Update, Delete (CRUD) operations for notes
# class NoteResource(Resource):
#     def get(self, note_id):
#         current_user = get_jwt_identity()
#         note = notes_collection.find_one({'_id': note_id, 'user_id': current_user['username']})
#         if note:
#             return {'note': note}, 200
#         return {'message': 'Note not found or access denied'}, 404


#     @jwt_required()
#     def put(self, note_id):
#         current_user = get_jwt_identity()
#         parser = reqparse.RequestParser()
#         parser.add_argument('title', required=True, help="Title field is required.")
#         parser.add_argument('content', required=True, help="Content field is required.")
#         data = parser.parse_args()

#         updated_note = {
#             'title': data['title'],
#             'content': data['content'],
#             'user_id': current_user['username'],
#         }
#         notes_collection.update_one({'_id': note_id, 'user_id': current_user['username']}, {'$set': updated_note})
#         return {'message': 'Note updated successfully'}, 200

#     @jwt_required()
#     def delete(self, note_id):
#         current_user = get_jwt_identity()
#         result = notes_collection.delete_one({'_id': note_id, 'user_id': current_user['username']})
#         if result.deleted_count > 0:
#             return {'message': 'Note deleted successfully'}, 200
#         return {'message': 'Note not found or access denied'}, 404

# api.add_resource(NoteResource, '/notes/<string:note_id>')

# class NoteResourcePost(Resource):
#     @jwt_required()
#     def post(self):
#         current_user = get_jwt_identity()
#         parser = reqparse.RequestParser()
#         parser.add_argument('title', required=True, help="Title field is required.")
#         parser.add_argument('content', required=True, help="Content field is required.")
#         data = parser.parse_args()

#         note = {
#             'title': data['title'],
#             'content': data['content'],
#             'user_id': current_user['username'],
#         }
#         result = notes_collection.insert_one(note)
#         return {'message': 'Note created successfully', 'note_id': str(result.inserted_id)}, 201

# api.add_resource(NoteResourcePost, '/notes')

# if __name__ == '__main__':
#     app.run(debug=True)
