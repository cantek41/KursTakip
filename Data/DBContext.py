from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

from Data.BaseEntity import Base
import Data.Entites

import os

basedir = os.path.realpath(os.path.abspath(os.path.dirname(__file__)) + '/../')

engine = create_engine('sqlite:///' + os.path.join(basedir, 'dataBase.db'))
Session = sessionmaker()
Session.configure(bind=engine)


def create_database(self):
    self.Base.metadata.create_all(engine)


if __name__ == '__main__':
    Base.metadata.create_all(engine)
