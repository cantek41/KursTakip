import Data.DBContext
import Data.Entites


class BaseService:
    session = Data.DBContext.Session()
    _entity = object

    def get_all(self):
        return self.session.query(self._entity).all()

    def get_by_id(self, id):
        return self.session.query(self._entity).filter_by(id=id).first()

    def add(self, entity):
        try:
            self.session.add(entity)
            self.session.commit()
        except Exception as ex:
            print(ex)
            self.session.rollback()

    def delete(self, entity):
        self.session.delete(entity)
        self.session.commit()

    def get_entity(self):
        return self._entity
