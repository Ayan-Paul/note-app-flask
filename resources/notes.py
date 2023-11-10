from flask_restful import Resource, reqparse
from flask_jwt_extended import get_jwt_identity, jwt_required
from bson import ObjectId

from db import notes_collection

class NoteResource(Resource):
    @jwt_required()
    def get(self, note_id):
        current_user = get_jwt_identity()
        try:
            note = notes_collection.find_one({'_id': ObjectId(note_id), 'user_id': current_user['username']})
            if note:
                note['_id'] = str(note['_id'])  # Convert ObjectId to string
                return {'note': note}, 200
            return {'message': 'Note not found or access denied'}, 404
        except:
            return {'message': 'Invalid note_id format'}, 400

    @jwt_required()
    def put(self, note_id):
        current_user = get_jwt_identity()
        parser = reqparse.RequestParser()
        parser.add_argument('title', required=True, help="Title field is required.")
        parser.add_argument('content', required=True, help="Content field is required.")
        data = parser.parse_args()

        updated_note = {
            'title': data['title'],
            'content': data['content'],
            'user_id': current_user['username'],
        }
        notes_collection.update_one({'_id': ObjectId(note_id), 'user_id': current_user['username']}, {'$set': updated_note})
        return {'message': 'Note updated successfully'}, 200

    @jwt_required()
    def delete(self, note_id):
        current_user = get_jwt_identity()
        result = notes_collection.delete_one({'_id': ObjectId(note_id), 'user_id': current_user['username']})
        if result.deleted_count > 0:
            return {'message': 'Note deleted successfully'}, 200
        return {'message': 'Note not found or access denied'}, 404


class NoteCreateResource(Resource):
    @jwt_required()
    def post(self):
        current_user = get_jwt_identity()
        parser = reqparse.RequestParser()
        parser.add_argument('title', required=True, help="Title field is required.")
        parser.add_argument('content', required=True, help="Content field is required.")
        data = parser.parse_args()

        note = {
            'title': data['title'],
            'content': data['content'],
            'user_id': current_user['username'],
        }
        result = notes_collection.insert_one(note)
        return {'message': 'Note created successfully', 'note_id': str(result.inserted_id)}, 201

