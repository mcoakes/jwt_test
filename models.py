# models.py

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import exc
import sys

db = SQLAlchemy()

class UserModel(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(120), unique = True, 
        nullable = False
    )
    password = db.Column(db.String(120), unique = True, 
        nullable = False
    )

    def save_to_db(self):
        try:
            db.session.add(self)
            db.session.commit()
        except exc.SQLAlchemyError as e:
            raise ValueError("Unable to create user.")
  
    @classmethod
    def find_by_username(cls, username):
        return cls.query.filter_by(username = username).first()

    @property
    def

class ModelHelper():
    pass
