from flask import request, jsonify
from Bussines.BaseService import BaseService
from flask_restful import Resource


class BaseApi(Resource):
    _service = BaseService()

    def get(self, id):
        result = self._service.get_by_id(id).to_json()
        return jsonify(result)

    def delete(self, id):
        entity = self._service.get_by_id(id)
        self._service.delete(entity)
        return "Ok", 200


class BaseApiList(Resource):
    _service = BaseService()

    def get(self):
        results = self._service.get_all()
        result = []
        for c in results:
            result.append(c.to_json())
        return jsonify({"result": result})

    def put(self):
        data = request.get_json()
        result = self._service.get_by_id(data['id'])
        result.update_columns(data)
        self._service.add(result)
        return jsonify(result.to_json())

    def post(self):
        data = request.get_json()
        result = self._service.get_entity().from_json(data)
        self._service.add(result)
        return jsonify(result.to_json())
