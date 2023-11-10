import os
from pymongo import MongoClient

# Set up MongoDB connection
client = MongoClient(os.getenv("DATABASE_URL"))
db = client['NoteApp']
users_collection = db['users']
notes_collection = db['notes']