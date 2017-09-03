from Api.BaseApi import BaseApi, BaseApiList
from Bussines.CourceService import CourseService


class TeacherApi(BaseApi):
    _service = CourseService()


class TeacherApiList(BaseApiList):
    _service = CourseService()


class CourseApi(BaseApi):
    _service = CourseService()


class CourseApiList(BaseApiList):
    _service = CourseService()
