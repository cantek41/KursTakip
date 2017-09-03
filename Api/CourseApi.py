from flask import Blueprint, request, jsonify
from Bussines.CourceService import CourseService
from Data.Entites import Course

simple_page = Blueprint('simple_page', __name__)

_service = CourseService()
route = '/Course'


@simple_page.route(route + '/<id>', methods=['GET'])
def get_by_id(id):
    result = _service.get_by_id(id).to_json()
    return jsonify(result)


@simple_page.route(route, methods=['GET'])
def get_all():
    results = _service.get_all()
    result = []
    for c in results:
        result.append(c.to_json())
    return jsonify({"result": result})


@simple_page.route(route, methods=['POST'])
def insert():
    data = request.get_json()
    new_course = Course(**data)
    _service.add(new_course)
    return "Ok", 200


@simple_page.route(route, methods=['PUT'])
def update():
    data = request.get_json()
    new_course = _service.get_by_id(data['id'])
    new_course.update_columns(data)
    _service.add(new_course)
    return "Ok", 200


@simple_page.route(route + '/<id>', methods=['DELETE'])
def delete(id):
    entity = _service.get_by_id(id)
    _service.delete(entity)
    return "Ok", 200
