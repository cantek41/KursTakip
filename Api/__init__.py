from flask import Flask, request, jsonify
import jwt
from functools import wraps

from flask_restful import Api
from flask_cors import CORS, cross_origin

from Data.Entites import User
from config import SECRET_KEY

from Api import Apies

app = Flask(__name__)


def create_app():
    app.config['SECRET_KEY'] = SECRET_KEY
    api = Api(app)

    set_route(api)
    return app


@app.after_request
def after_request(response):
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
    response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE')
    return response


def set_route(api):
    api.add_resource(Apies.TeacherApiList, '/teacher')
    api.add_resource(Apies.TeacherApi, '/teacher/<id>')

    api.add_resource(Apies.CourseApiList, '/course')
    api.add_resource(Apies.CourseApi, '/course/<id>')

    api.add_resource(Apies.StudentApiList, '/student')
    api.add_resource(Apies.StudentApi, '/student/<id>')

    api.add_resource(Apies.CourseStudentApiList, '/course/student')
    api.add_resource(Apies.CourseStudentApi, '/course/student/<id>')

    api.add_resource(Apies.GradeApiList, '/grade')
    api.add_resource(Apies.GradeApi, '/grade/<id>')

    api.add_resource(Apies.RollCallApiList, '/course/rollcall')
    api.add_resource(Apies.RollCallApi, '/course/rollcall/<id>')

    api.add_resource(Apies.DocumentApiList, '/document')
    api.add_resource(Apies.DocumentApi, '/document/<id>')

    api.add_resource(Apies.CourseQuizApiList, '/course/quiz')
    api.add_resource(Apies.CourseQuizApi, '/course/quiz/<id>')


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
