from Data import Entites
from Bussines.BaseService import BaseService
from sqlalchemy.sql import func


class CourseService(BaseService):
    _entity = Entites.Course


class TeacherService(BaseService):
    _entity = Entites.Teacher


class StudentService(BaseService):
    _entity = Entites.Student

    def get_by_identity(self, identity):
        results = self.session.query(self._entity).filter_by(identity=identity).first()
        return results


class CourseStudentService(BaseService):
    _entity = Entites.CourseStudent

    def get_by_course(self, course_id):
        results = self.session.query(self._entity).filter_by(Course_id=course_id).all()
        return results


class GradeService(BaseService):
    _entity = Entites.Grade


class RollCallService(BaseService):
    _entity = Entites.RollCall

    _courseEntity = Entites.CourseStudent

    def get_by_course(self, course_id):
        results = self.session.query(self._courseEntity).filter_by(Course_id=course_id).all()
        for item in results:
            item.total = self.session.query(self._entity, func.sum(self._entity.hour).label("score")).filter_by(
                Course_id=course_id,
                Student_id=item.Student_id).first().score
        return results


class CourseQuizService(BaseService):
    _entity = Entites.CourseQuiz

    def get_by_course(self, course_id):
        results = self.session.query(self._entity).filter_by(Course_id=course_id).all()
        return results


class DocumentService(BaseService):
    _entity = Entites.Document
