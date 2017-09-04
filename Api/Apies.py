from flask import jsonify

from Api.BaseApi import BaseApi, BaseApiList
from Bussines import Services


class TeacherApi(BaseApi):
    _service = Services.TeacherService()


class TeacherApiList(BaseApiList):
    _service = Services.TeacherService()


class CourseApi(BaseApi):
    _service = Services.CourseService()


class CourseApiList(BaseApiList):
    _service = Services.CourseService()


class StudentApi(BaseApi):
    _service = Services.StudentService()


class StudentApiList(BaseApiList):
    _service = Services.StudentService()


class CourseStudentApi(BaseApi):
    _service = Services.CourseStudentService()


class CourseStudentApiList(BaseApiList):
    _service = Services.CourseStudentService()


class GradeApi(BaseApi):
    _service = Services.GradeService()


class GradeApiList(BaseApiList):
    _service = Services.GradeService()


class RollCallApi(BaseApi):
    _service = Services.RollCallService()


class RollCallApiList(BaseApiList):
    _service = Services.RollCallService()


class DocumentApi(BaseApi):
    _service = Services.DocumentService()


class DocumentApiList(BaseApiList):
    _service = Services.DocumentService()


class CourseQuizApi(BaseApi):
    _service = Services.CourseQuizService()

    def get(self, id):
        results = self._service.get_by_course(id)
        result = []
        for c in results:
            result.append(c.to_json())
        return jsonify({"result": result})


class CourseQuizApiList(BaseApiList):
    _service = Services.CourseQuizService()
