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

    def get(self):
        results = self._service.get_all()
        result = []
        for c in results:
            temp = c.to_json()
            temp["teacher"] = ""
            if c.teacher:
                temp["teacher"] = c.teacher.name
            result.append(temp)
        return jsonify({"result": result})


class StudentApi(BaseApi):
    _service = Services.StudentService()

    def get(self, id):
        result = self._service.get_by_identity(id)
        if result:
            return jsonify(result.to_json())
        else:
            return {}


class StudentApiList(BaseApiList):
    _service = Services.StudentService()


class CourseStudentApi(BaseApi):
    _service = Services.CourseStudentService()

    def get(self, id):
        results = self._service.get_by_course(id)
        result = []
        for c in results:
            temp = c.Student.to_json()
            temp["delete_id"] = c.id
            result.append(temp)
        return jsonify({"result": result})


class CourseStudentApiList(BaseApiList):
    _service = Services.CourseStudentService()


class GradeApi(BaseApi):
    _service = Services.GradeService()


class GradeApiList(BaseApiList):
    _service = Services.GradeService()


class RollCallApi(BaseApi):
    _service = Services.RollCallService()

    def get(self, id):
        results = self._service.get_by_course(id)
        result = []
        for c in results:
            item = {"id": c.Student.id, "name": c.Student.name, "surname": c.Student.surname, "total": c.total}
            result.append(item)
        return jsonify({"result": result})


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
            result.append(c.Student.to_json())
        return jsonify({"result": result})


class CourseQuizApiList(BaseApiList):
    _service = Services.CourseQuizService()
