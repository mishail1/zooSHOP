import sqlalchemy
from .db_session import SqlAlchemyBase
from flask_login import UserMixin


class User(SqlAlchemyBase, UserMixin):
    __tablename__ = 'users'

    id = sqlalchemy.Column(sqlalchemy.Integer,
                           primary_key=True, autoincrement=True)
    email = sqlalchemy.Column(sqlalchemy.String(120), index=True, unique=True)
    password = sqlalchemy.Column(sqlalchemy.String(128), nullable=True)

    def __repr__(self):
        return '<User {}>'.format(self.username)

    def get_id(self):
        return str(self.id)