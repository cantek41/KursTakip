from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

from Data.BaseEntity import Base
import Data.Entites

from config import db_name

engine = create_engine(db_name)
Session = sessionmaker()
Session.configure(bind=engine)


def create_database(self):
    self.Base.metadata.create_all(engine)


if __name__ == '__main__':
    Base.metadata.create_all(engine)
