from sqlalchemy import Column, Integer
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class BaseEntity(Base):
    __abstract__ = True
    id = Column(Integer, primary_key=True)

    def to_json(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}
