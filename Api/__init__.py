from flask import Flask, request, jsonify
import jwt
from functools import wraps

from flask_restful import Api

from Data.Entites import User
from config import SECRET_KEY

from Api import Apies


def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = SECRET_KEY
    api = Api(app)
    set_route(api)
    return app


def set_route(api):
    api.add_resource(Apies.TeacherApiList, '/teacher')
    api.add_resource(Apies.TeacherApi, '/teacher/<id>')
    api.add_resource(Apies.CourseApiList, '/course')
    api.add_resource(Apies.CourseApi, '/course/<id>')


def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = None

        if 'x-access-token' in request.headers:
            token = request.headers['x-access-token']

        if not token:
            return jsonify({'message': 'Token is missing'}), 401

        try:

            data = jwt.decode(token, SECRET_KEY)
            current_user = User.query.filter_by(public_id=data['public_id']).first()

        except Exception:
            return jsonify({'message': 'Token is invalid!!'}), 401

        return f(current_user, *args, **kwargs)

    return decorated
