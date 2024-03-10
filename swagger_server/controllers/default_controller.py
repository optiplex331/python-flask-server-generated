import connexion
import six

from swagger_server.models.student import Student  # noqa: E501
from swagger_server import util

from swagger_server.service.student_service import *


def add_student(body=None):  # noqa: E501
        """Add a new student

            Adds an item to the system # noqa: E501

            :param body: Student item to add
            :type body: dict | bytes

            :rtype: float
            """
        if connexion.request.is_json:
            body = connexion.request.get_json()  # Directly use the JSON from the request
            result, status = add(body)  # Pass the dictionary directly to the service
            return result, status
        return 'Invalid input, body is not JSON', 400  # Return error if request is not in JSON format


def delete_student(student_id):  # noqa: E501
    """deletes a student

    Deletes a single student.  # noqa: E501

    :param student_id: the unique identifier
    :type student_id: float

    :rtype: None
    """
    return delete(student_id)


def get_student_by_id(student_id):  # noqa: E501
    """gets student

    Returns a single student  # noqa: E501

    :param student_id: the uid
    :type student_id: float

    :rtype: Student
    """
    return get_by_id(student_id)
