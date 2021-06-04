import sqlalchemy
from .db_session import SqlAlchemyBase


class Tovars(SqlAlchemyBase):
    __tablename__ = 'tovars'

    id = sqlalchemy.Column(sqlalchemy.Integer,
                           primary_key=True, autoincrement=True)
    user_id = sqlalchemy.Column(sqlalchemy.Integer,
                                sqlalchemy.ForeignKey("users.id"))
    user = sqlalchemy.orm.relation('User')
    tovar_id = sqlalchemy.Column(sqlalchemy.Integer,
                                sqlalchemy.ForeignKey("allTovars.id"))
    allTovars = sqlalchemy.orm.relation('ALLtovars')

    def get_id(self):
        return str(self.id)

