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
