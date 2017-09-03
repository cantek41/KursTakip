from sqlalchemy import Column, Integer, Unicode, String, Boolean, SMALLINT, Date, ForeignKey
from sqlalchemy.orm import relationship

from Data.BaseEntity import BaseEntity


class Course(BaseEntity):
    __tablename__ = "Course"
    name = Column(String(50))
    status = Column(Boolean)
    teacher = relationship("Teacher", back_populates="Course")
    teacher_id = Column(Integer, ForeignKey('Teacher.id'))
    hour = Column(Integer)
    qouta = Column(SMALLINT)
    end_date = Column(Date)
    start_date = Column(Date)


class Teacher(BaseEntity):
    __tablename__ = "Teacher"
    name = Column(String(20))
    surname = Column(String(20))
    identity = Column(String(11))


class Student(BaseEntity):
    __tablename__ = "Student"
    name = Column(String(20))
    surname = Column(String(20))
    identity = Column(String(11))
    grade = Column(String(5))


class CourseStudent(BaseEntity):
    __tablename__ = "CourseStudent"
    Course = relationship("Course", back_populates="CourseStudent")
    Course_id = Column(Integer, ForeignKey('Course.id'))
    Student = relationship("Student", back_populates="CourseStudent")
    Student_id = Column(Integer, ForeignKey('Student.id'))

class Grade(BaseEntity):
    __tablename__ = "Grade"
    name = Column(String(20))
    year = Column(Integer)


class RollCall(BaseEntity):
    __tablename__ = "RollCall"
    Course = relationship("Course", back_populates="RollCall")
    Course_id = Column(Integer, ForeignKey('Course.id'))
    Student = relationship("Student", back_populates="RollCall")
    Student_id = Column(Integer, ForeignKey('Student.id'))
    day_date = Column(Date)


class CourseQuiz(BaseEntity):
    __tablename__ = "CourseQuiz"
    Course = relationship("Course", back_populates="CourseQuiz")
    Course_id = Column(Integer, ForeignKey('Course.id'))
    Student = relationship("Student", back_populates="CourseQuiz")
    Student_id = Column(Integer, ForeignKey('Student.id'))
    score = Column(SMALLINT)


class Document(BaseEntity):
    __tablename__ = "Document"
    Course = relationship("Course", back_populates="Document")
    Course_id = Column(Integer, ForeignKey('Course.id'))
    Student = relationship("Student", back_populates="Document")
    Student_id = Column(Integer, ForeignKey('Student.id'))
    day_date = Column(Date)
    document_Id = Column(String(20))
    isPrint = Column(Boolean)
    isTake = Column(Boolean)
