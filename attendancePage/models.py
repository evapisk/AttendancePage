from flask_sqlalchemy import SQLAlchemy
from . import db
from flask_login import UserMixin
import json

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True) # primary keys are required by SQLAlchemy
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    name = db.Column(db.String(1000))

class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)  # primary keys are required by SQLAlchemy
    schoolId = db.Column(db.String(100))
    name = db.Column(db.String(1000))
    year = db.Column(db.Integer)
    sport = db.Column(db.String(20))
    gender = db.Column(db.String(10))

    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}

    def __repr__(self):
        return '<Student {}>'.format(self.name)


