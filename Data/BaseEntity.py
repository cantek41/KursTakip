import json
from collections import namedtuple

from sqlalchemy import Column, Integer
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class BaseEntity(Base):
    __abstract__ = True
    id = Column(Integer, primary_key=True)

    def to_json(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}

    @classmethod
    def from_json(cls, data):
        # json_dict = json.loads(data)
        # return cls(**json_dict)
        return cls(**data)

    def update_columns(self, data):
        for c in self.__table__.columns:
            setattr(self, str(c.name), data[c.name])
        return self
