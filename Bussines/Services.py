from Data.Entites import Course, Teacher
from Bussines.BaseService import BaseService


class CourseService(BaseService):
    _entity = Course


class TeacherService(BaseService):
    _entity = Teacher
