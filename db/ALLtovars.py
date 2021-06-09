import sqlalchemy
from .db_session import SqlAlchemyBase


class ALLtovars(SqlAlchemyBase):
    __tablename__ = 'allTovars'

    id = sqlalchemy.Column(sqlalchemy.Integer,
                           primary_key=True, autoincrement=True)
    name_tovar = sqlalchemy.Column(sqlalchemy.String(120), index=True, unique=True)
    price = sqlalchemy.Column(sqlalchemy.String, nullable=True)

    link_img = sqlalchemy.Column(sqlalchemy.String)

    def get_id(self):
        return str(self.id)
