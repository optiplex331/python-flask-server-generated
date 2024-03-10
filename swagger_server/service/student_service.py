import os
from pymongo import MongoClient
from bson.objectid import ObjectId

# MongoDB setup
client = MongoClient('mongodb://localhost:27017/')  # Connect to your MongoDB server
db = client.school  # Use (or create) a database called 'school'
student_collection = db.students  # Use (or create) a collection called 'students'


def add(student=None):
    # Check if student already exists
    if student_collection.find_one({'first_name': student['first_name'], 'last_name': student['last_name']}):
        return 'already exists', 409

    # Insert new student
    result = student_collection.insert_one(student)
    return str(result.inserted_id), 200  # Convert ObjectId to string


def get_by_id(student_id=None, subject=None):
    # MongoDB uses '_id' as default key for the document identifier
    student = student_collection.find_one({'_id': ObjectId(student_id)})
    if not student:
        return 'not found', 404

    student['student_id'] = str(student['_id'])  # Convert ObjectId to string
    del student['_id']  # Remove the original MongoDB identifier for response
    return student, 200


def delete(student_id=None):
    result = student_collection.delete_one({'_id': ObjectId(student_id)})
    if result.deleted_count == 0:
        return 'not found', 404
    return student_id, 200
