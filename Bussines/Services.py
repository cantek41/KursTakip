from Data import Entites
from Bussines.BaseService import BaseService


class CourseService(BaseService):
    _entity = Entites.Course



class TeacherService(BaseService):
    _entity = Entites.Teacher


class StudentService(BaseService):
    _entity = Entites.Student


class CourseStudentService(BaseService):
    _entity = Entites.CourseStudent


class GradeService(BaseService):
    _entity = Entites.Grade


class RollCallService(BaseService):
    _entity = Entites.RollCall


class CourseQuizService(BaseService):
    _entity = Entites.CourseQuiz

    def get_by_course(self, course_id):
        results = self.session.query(self._entity).filter_by(Course_id=course_id).all()
        return results


class DocumentService(BaseService):
    _entity = Entites.Document
