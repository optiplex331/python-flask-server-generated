import os

from pymongo import MongoClient

# MongoDB setup
mongo_uri = os.getenv('MONGO_URI', 'mongodb://localhost:27017/school')
client = MongoClient(mongo_uri)
db = client.school
student_collection = db.students


def add(student=None):
    # Directly use the student dictionary for MongoDB operations
    # Check if student already exists based on 'first_name' and 'last_name'
    if student_collection.find_one({'first_name': student['first_name'], 'last_name': student['last_name']}):
        return {'message': 'Student already exists'}, 409

    # Insert new student
    result = student_collection.insert_one(student)
    # Return the student_id (MongoDB _id field) as a string
    return {'student_id': student['student_id']}, 200


def get_by_id(student_id=None):
    student = student_collection.find_one({'student_id': student_id})
    if not student:
        return {'message': 'Student not found'}, 404
    if '_id' in student:
        del student['_id']
    return student, 200


def delete(student_id=None):
    result = student_collection.delete_one({'student_id': student_id})
    if result.deleted_count == 0:
        return {'message': 'Student not found'}, 404
    return {'message': 'Student deleted successfully'}, 200
